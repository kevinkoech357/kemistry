from kemistry import db
from sqlalchemy import func
from datetime import timezone
from nanoid import generate as generate_nanoid

ALPHANUM = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-"


class BaseModel(db.Model):
    """
    Create a Base to be inherited by other class models.
    """

    __abstract__ = True

    id = db.Column(
        db.String(10),
        primary_key=True,
        index=True,
        default=generate_nanoid(ALPHANUM, 10),
        nullable=False,
    )
    created_at = db.Column(
        db.DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
