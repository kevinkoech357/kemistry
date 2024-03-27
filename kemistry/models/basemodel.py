from kemistry import db
from sqlalchemy import func
from uuid import uuid4


def generate_uuid():
    """
    Generate a unique id using uuid4()
    """
    return uuid4().hex


class BaseModel(db.Model):
    """
    Create a Base to be inherited by other class models.
    """

    __abstract__ = True

    id = db.Column(
        db.String(32),
        primary_key=True,
        unique=True,
        index=True,
        default=generate_uuid,
        nullable=False,
    )
    created_at = db.Column(
        db.DateTime(timezone=True), default=func.now(), nullable=False
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
