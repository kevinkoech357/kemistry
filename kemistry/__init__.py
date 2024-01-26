# Flask extensions
from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from flask_moment import Moment
from flask_session import Session
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_wtf import CSRFProtect

# App modules
from kemistry.config import App_Config
from kemistry.models.basemodel import Base

# Initializing extension objects
db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()
bootstrap = Bootstrap5()
migrate = Migrate()
sess = Session()
bcrypt = Bcrypt()
moment = Moment()


def create_app():
    """
    Create and return an app instance of Flask.
    """
    app = Flask(__name__)

    # Loading local config into app
    app.config.from_object(App_Config)

    # Allow URLs with or without trailing slashes
    app.url_map.strict_slashes = False

    # Setting CORS
    CORS(app, supports_credentials=True)

    # Lazy loading the extensions
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app, db)
    sess.init_app(app)
    bcrypt.init_app(app)
    moment.init_app(app)

    # Import blueprints
    from kemistry.auth.routes import auth
    from kemistry.user.routes import user

    # Register blueprints
    app.register_blueprint(auth)
    app.register_blueprint(user)

    # Import User
    from kemistry.models.user import User

    with app.app_context():
        # Create database tables
        db.create_all()
        print("Database created successfully")

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @login_manager.unauthorized_handler
    def unauthorized():
        flash("Please log in to access this page.", "warning")
        return redirect(url_for("auth.login"))

    # Error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template("500.html"), 500

    return app
