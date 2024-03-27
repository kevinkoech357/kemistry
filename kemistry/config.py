import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class App_Config:
    """
    Configurations for the app.
    """

    # Secret key for Flask app
    SECRET_KEY = os.environ.get("SECRET_KEY", "kemistry2024")

    # SQLAlchemy configurations
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI", "sqlite:///kemistry.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
    }

    # Bootstrap config
    BOOTSTRAP_BOOTSWATCH_THEME = "superhero"
    BOOTSTRAP_SERVE_LOCAL = True

    # Flask Admin
    FLASK_ADMIN_SWATCH = "superhero"

    # Flask-Security password configurations
    SECURITY_PASSWORD_SALT = os.environ.get(
        "SECURITY_PASSWORD_SALT", "146585145368132386173505678016728509634"
    )
    SECURITY_PASSWORD_HASH = "argon2"

    # Session and remember cookie settings
    REMEMBER_COOKIE_SAMESITE = "strict"
    SESSION_COOKIE_SAMESITE = "strict"

    # Flask-Security feature flags
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_CONFIRMABLE = True
    SECURITY_REGISTERABLE = True

    # Views for redirects
    SECURITY_POST_LOGIN_VIEW = "/"
    SECURITY_DEFAULT_REMEMBER_ME = True
    SECURITY_POST_CONFIRM_VIEW = "/login"
    SECURITY_CONFIRM_ERROR_VIEW = "/login"
    SECURITY_CONFIRM_EMAIL_WITHIN = "1 days"
    SECURITY_AUTO_LOGIN_AFTER_CONFIRM = False
    SECURITY_RESET_VIEW = "/reset"
    SECURITY_RESET_ERROR_VIEW = "/reset"
    SECURITY_EMAIL_SUBJECT_REGISTER = "Welcome to Kemistry."

    # CSRF protection settings
    SECURITY_CSRF_PROTECT_MECHANISMS = ["session", "basic"]
    SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS = True
    SECURITY_CSRF_COOKIE_NAME = "XSRF-TOKEN"
    WTF_CSRF_CHECK_DEFAULT = False

    # User identity attributes for Flask-Security
    # SECURITY_USER_IDENTITY_ATTRIBUTES = ["email"]

    # User model uniquifier attribute for Flask-Security
    USER_MODEL_FS_UNIQUIFER = "fs_uniquifier"

    # EMAIL CONFIG
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")

    # Username Config
    SECURITY_USERNAME_ENABLE = True
    SECURITY_USERNAME_REQUIRED = True

    # 2-FA
    SECURITY_TWO_FACTOR = True
    SECURITY_TWO_FACTOR_REQUIRED = True
    SECURITY_TWO_FACTOR_ENABLED_METHODS = ["authenticator", "email"]
    SECURITY_TWO_FACTOR_ALWAYS_VALIDATE = False
    SECURITY_TWO_FACTOR_LOGIN_VALIDITY = "1 week"
    SECURITY_TWO_FACTOR_RESCUE_EMAIL = True
    SECURITY_TWO_FACTOR_RESCUE_MAIL = os.environ.get("ADMIN_EMAIL")
    SECURITY_MULTI_FACTOR_RECOVERY_CODES = False

    # TOTP (Time-based One-Time Password) settings
    SECURITY_TOTP_SECRETS = json.loads(os.getenv("SECURITY_TOTP_SECRETS", "{}"))
    SECURITY_TOTP_ISSUER = "Kemistry"

    # Uploads dir
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER")
