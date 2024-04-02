import os
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from flask_moment import Moment
from flask_session import Session
from flask_cors import CORS
from flask_wtf import CSRFProtect
from flask_security.core import Security
from flask_security.utils import hash_password
from flask_security.datastore import SQLAlchemyUserDatastore
from flask_mailman import Mail
from flask_admin import Admin
from flask_admin import helpers as admin_helpers


# App modules
from kemistry.config import App_Config
from kemistry.async_email import MyMailUtil
from kemistry.logger import configure_logging


# Initializing extension objects
db = SQLAlchemy()
bootstrap = Bootstrap5()
migrate = Migrate()
sess = Session()
moment = Moment()
mail = Mail()
admin = Admin(name="Kemistry", template_mode="bootstrap4")


def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for,
    )


def create_app():
    """
    Create and return an app instance of Flask.
    """
    # Import user and role models
    from kemistry.models.user import User
    from kemistry.models.role import Role
    from kemistry.super_admin.routes import AnalyticsView

    # Import extended register form
    from kemistry.forms.form import ExtendedRegisterForm

    app = Flask(__name__)

    # Loading local config into app
    app.config.from_object(App_Config)
    app.config["SECURITY_CONFIRM_REGISTER_FORM"] = ExtendedRegisterForm

    # Allow URLs with or without trailing slashes
    app.url_map.strict_slashes = False

    # Setting CORS
    CORS(app, supports_credentials=True)

    CSRFProtect(app)

    # Lazy loading the extensions
    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    moment.init_app(app)

    # Set up logging
    configure_logging(app)

    admin.add_view(AnalyticsView(name="Analytics", endpoint="analytics"))

    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(
        app,
        user_datastore,
        register_form=ExtendedRegisterForm,
        mail_util_cls=MyMailUtil,
    )

    # Import blueprints
    from kemistry.user.routes import user
    from kemistry.post.routes import post

    # Register blueprints
    app.register_blueprint(user)
    app.register_blueprint(post)

    # one time setup
    with app.app_context():
        db.create_all()
        print("Created db successfully")
        # Create user role
        app.security.datastore.find_or_create_role(
            name="user",
            permissions={"user-read", "user-write", "user-edit", "user-delete"},
        )
        db.session.commit()
        # Create admin role
        app.security.datastore.find_or_create_role(
            name="admin",
            permissions={
                "admin-read",
                "admin-write",
                "admin-edit",
                "admin-delete",
            },
        )
        db.session.commit()

        # Create admin user
        admin_email = os.environ.get("ADMIN_EMAIL")
        admin_password = os.environ.get("ADMIN_PASSWORD")
        admin_username = os.environ.get("ADMIN_USERNAME")

        if admin_email and admin_password:
            if not app.security.datastore.find_user(email=admin_email):
                app.security.datastore.create_user(
                    email=admin_email,
                    username=admin_username,
                    password=hash_password(admin_password),
                    roles=["admin"],
                )
                db.session.commit()
            else:
                print(f"Admin user with email {admin_email} already exists.")
        else:
            print(
                "ADMIN_EMAIL, ADMIN_PASSWORD and ADMIN_USERNAME \
                environment variables must be set."
            )

    app.context_processor(security_context_processor)

    # Error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    @app.errorhandler(403)
    def forbidden(e):
        return render_template("403.html"), 403

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template("500.html"), 500

    return app
