from kemistry import db
from datetime import datetime, timezone
from nanoid import generate


class BaseModel(db.Model):
    """
    Create a Base to be inherited by other class models.
    """

    __abstract__ = True

    id = db.Column(db.String(10), primary_key=True, default=generate, index=True)
    created_at = db.Column(
        db.DateTime(timezone=True), default=datetime.now(timezone.utc)
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.id = generate("1234567890", 10)
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)
