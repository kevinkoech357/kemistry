import os

# Load environment variables from .env file
# load_dotenv(".env")


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

    # Flask-Security configurations
    SECURITY_PASSWORD_SALT = os.environ.get(
        "SECURITY_PASSWORD_SALT", "146585145368132386173505678016728509634"
    )

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
    SECURITY_POST_CONFIRM_VIEW = "/confirmed"
    SECURITY_CONFIRM_ERROR_VIEW = "/confirm-error"
    SECURITY_RESET_VIEW = "/reset-password"
    SECURITY_RESET_ERROR_VIEW = "/reset-password-error"
    SECURITY_REDIRECT_BEHAVIOR = "spa"

    # CSRF protection settings
    SECURITY_CSRF_PROTECT_MECHANISMS = ["session", "basic"]
    SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS = True
    SECURITY_CSRF_COOKIE_NAME = "XSRF-TOKEN"
    WTF_CSRF_CHECK_DEFAULT = False

    # TOTP (Time-based One-Time Password) settings
    SECURITY_TOTP_SECRETS = {"1": "TjQ9Qa31VOrfEzuPy4VHQWPCTmRzCnFzMKLxXYiZu9B"}
    SECURITY_TOTP_ISSUER = "kemistry2024"

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
