from kemistry.models.basemodel import BaseModel
from flask_security.core import UserMixin
from kemistry import db


class User(BaseModel, UserMixin):
    """
    User model representing application users.
    """

    __tablename__ = "user"

    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True, nullable=False)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(64), unique=True, nullable=False)
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship(
        "Role", secondary="roles_users", backref=db.backref("users", lazy="dynamic")
    )

    def __init__(self, **kwargs):
        """
        Constructor for User class.

        Parameters:
        - kwargs: Keyword arguments representing user attributes
        """
        super().__init__(**kwargs)
        self.first_name = kwargs.get("first_name", "")
        self.last_name = kwargs.get("last_name", "")
        self.qualification = kwargs.get("qualification", "")
        self.university = kwargs.get("university", "")
        self.email = kwargs.get("email", "")
        self.username = kwargs.get("username", "")
        self.password = kwargs.get("password", "")
        self.active = kwargs.get("active", False)
        self.fs_uniquifier = kwargs.get("fs_uniquifier", "")
        self.last_login_at = kwargs.get("last_login_at", None)
        self.last_login_ip = kwargs.get("last_login_ip", "")
        self.current_login_at = kwargs.get("current_login_at", None)
        self.current_login_ip = kwargs.get("current_login_ip", "")
        self.login_count = kwargs.get("login_count", 0)
        self.confirmed_at = kwargs.get("confirmed_at", None)
