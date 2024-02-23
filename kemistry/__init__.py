# Flask extensions
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from flask_moment import Moment
from flask_session import Session
from flask_cors import CORS
from flask_wtf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_security.core import Security
from flask_security import hash_password
from flask_security.datastore import SQLAlchemyUserDatastore
from flask_mailman import Mail

# App modules
from kemistry.config import App_Config


# Initializing extension objects
db = SQLAlchemy()
bootstrap = Bootstrap5()
migrate = Migrate()
sess = Session()
moment = Moment()
bcrypt = Bcrypt()
mail = Mail()


def create_app():
    """
    Create and return an app instance of Flask.
    """
    # Import user and role models
    from kemistry.models.user import User
    from kemistry.models.role import Role

    # Import extended register form
    from kemistry.forms.forms import ExtendedRegisterForm

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
    bcrypt.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, user_datastore, register_form=ExtendedRegisterForm)

    # Import blueprints
    from kemistry.user.routes import user

    # Register blueprints
    app.register_blueprint(user)

    # one time setup
    with app.app_context():
        db.create_all()
        print("Created db successfully")
        # Create a user and role to test with
        app.security.datastore.find_or_create_role(
            name="user", permissions={"user-read", "user-write"}
        )
        db.session.commit()
        if not app.security.datastore.find_user(email="test@me.com"):
            app.security.datastore.create_user(
                email="test@me.com", password=hash_password("password"), roles=["user"]
            )
            db.session.commit()

    # Error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template("500.html"), 500

    return app
