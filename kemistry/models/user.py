from flask_security.core import UserMixin
from kemistry.models.basemodel import BaseModel
from kemistry import db, admin
from kemistry.models.post import Post
from kemistry.super_admin.view_models import UserView
from hashlib import md5


class User(BaseModel, UserMixin):
    """
    User model representing application users.
    """

    __tablename__ = "user"

    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    qualification = db.Column(db.String(255))
    university = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True, nullable=False)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(100), unique=True, nullable=False)
    last_login_at = db.Column(db.DateTime(timezone=True))
    current_login_at = db.Column(db.DateTime(timezone=True))
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    confirmed_at = db.Column(db.DateTime(timezone=True))
    bio = db.Column(
        db.Text, default="A chemistry enthusiast ready to explore the world of science."
    )
    profile_image = db.Column(db.String(255))
    tf_primary_method = db.Column(db.String(64), nullable=True)
    tf_totp_secret = db.Column(db.String(255), nullable=True)

    roles = db.relationship(
        "Role", secondary="roles_users", backref=db.backref("users", lazy="dynamic")
    )

    # Relationships
    posts = db.relationship(
        "Post", back_populates="author", cascade="all, delete-orphan"
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
        self.bio = kwargs.get("bio", "")
        self.profile_image = kwargs.get("profile_image", "")
        self.tf_primary_method = kwargs.get("tf_primary_method", "")
        self.tf_totp_secret = kwargs.get("tf_totp_secret", "")

        if not self.profile_image:
            self.profile_image = self.avatar(128)

    def avatar(self, size):
        """
        Generate a Gravatar image URL for the user's avatar.

        Args:
            size (int): The size of the avatar image.

        Returns:
            str: The URL of the Gravatar image.

        """
        digest = md5(self.email.lower().encode("utf-8")).hexdigest()

        return f"https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}"


admin.add_view(UserView(User, db.session))
