from kemistry.models.basemodel import BaseModel
from kemistry import db
from flask_security.core import RoleMixin
from flask_security import AsaList
from sqlalchemy.ext.mutable import MutableList


class Role(BaseModel, RoleMixin):
    """
    Role model representing user roles in the application.
    """

    __tablename__ = "role"

    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    permissions = db.Column(MutableList.as_mutable(AsaList()), nullable=True)

    def __init__(
        self,
        name="user",
        description="Read, write, and delete their own posts",
        permissions=["user-read", "user-write", "delete-own-post"],
    ):
        """
        Constructor for Role class.

        Parameters:
        - name: Name of the role (default is "user")
        - description: Description of the role (default is "Read, write, and delete their own posts")
        - permissions: List of permissions associated with the role (default is ["user-read", "user-write", "delete-own-post"])
        """
        super().__init__()
        self.name = name
        self.description = description
        self.permissions = permissions


class RolesUsers(db.Model):
    """
    Association table between users and roles.
    """

    __tablename__ = "roles_users"

    user_id = db.Column(
        "user_id", db.String(), db.ForeignKey("user.id"), primary_key=True
    )
    role_id = db.Column(
        "role_id", db.String(), db.ForeignKey("role.id"), primary_key=True
    )

    def __init__(self, user_id, role_id):
        """
        Constructor for RolesUsers class.

        Parameters:
        - user_id: User ID
        - role_id: Role ID
        """
        self.user_id = user_id
        self.role_id = role_id
