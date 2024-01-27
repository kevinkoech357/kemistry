import os
from dotenv import load_dotenv

# load_dotenv(".env")


class App_Config:
    """
    Configurations for the app.
    """

    # Secret key
    SECRET_KEY = os.environ.get("SECRET_KEY", "kemistry2024")
    # Sqlachemy config
    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///kemistry.db")
    SQLALCHEMY_DATABASE_URI = "sqlite:///kemistry.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
    }
    # Bootstrap config
    BOOTSWATCH_THEME = "flatly"
    BOOTSWATCH_SERVE_LOCAL = True

    SECURITY_PASSWORD_SALT = os.environ.get(
        "SECURITY_PASSWORD_SALT", "146585145368132386173505678016728509634"
    )
    # have session and remember cookie be samesite (flask/flask_login)
    REMEMBER_COOKIE_SAMESITE = "strict"
    SESSION_COOKIE_SAMESITE = "strict"
    # Turn on all the great Flask-Security features
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_CONFIRMABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_UNIFIED_SIGNIN = True
    # These need to be defined to handle redirects
    # As defined in the API documentation - they will receive the relevant context
    SECURITY_POST_CONFIRM_VIEW = "/confirmed"
    SECURITY_CONFIRM_ERROR_VIEW = "/confirm-error"
    SECURITY_RESET_VIEW = "/reset-password"
    SECURITY_RESET_ERROR_VIEW = "/reset-password-error"
    SECURITY_REDIRECT_BEHAVIOR = "spa"
    # CSRF protection is critical for all session-based browser UIs
    # enforce CSRF protection for session / browser - but allow token-based
    # API calls to go through
    SECURITY_CSRF_PROTECT_MECHANISMS = ["session", "basic"]
    SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS = True
    # Send Cookie with csrf-token. This is the default for Axios and Angular.
    SECURITY_CSRF_COOKIE_NAME = "XSRF-TOKEN"
    WTF_CSRF_CHECK_DEFAULT = False

    # Generate a good totp secret using: passlib.totp.generate_secret()
    SECURITY_TOTP_SECRETS = {"1": "TjQ9Qa31VOrfEzuPy4VHQWPCTmRzCnFzMKLxXYiZu9B"}
    SECURITY_TOTP_ISSUER = "kemistry2024"
