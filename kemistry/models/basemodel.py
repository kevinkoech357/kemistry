from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime, timezone
import sqlalchemy.orm as so
from nanoid import generate


class Base(DeclarativeBase):
    """
    Create a Base to be inherited by other python classess.
    """

    __abstract__ = True

    id: Mapped[str] = mapped_column(
        primary_key=True,
        default=lambda: generate("1234567890abcdef", 10),
        nullable=False,
    )
    created_at: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at: so.Mapped[datetime] = so.mapped_column(
        index=True,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    def __init__(self):
        self.id = generate("1234567890", 10)
        created_at = datetime.now(timezone.utc)
        updated_at = datetime.now(timezone.utc)
