from kemistry.models.basemodel import Base
from kemistry import db
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin


class User(Base, db.Model, UserMixin):
    """
    Define modelling schema for User table.
    """

    __tablename__ = "users"

    username: so.Mapped[str] = so.mapped_column(
        sa.String(21), index=True, unique=True, nullable=False
    )
    first_name: so.Mapped[str] = so.mapped_column(sa.String(12), nullable=False)
    last_name: so.Mapped[str] = so.mapped_column(sa.String(12), nullable=False)
    email: so.Mapped[str] = so.mapped_column(
        sa.String(42), index=True, unique=True, nullable=False
    )
    password: so.Mapped[Optional[str]] = so.mapped_column(sa.String(42), nullable=False)

    def __init__(self, username, email, password):
        super().__init__()
        username = self.username
        email = self.email
        password = self.password

    def __repr__(self):
        return "<User {}>".format(self.username)
