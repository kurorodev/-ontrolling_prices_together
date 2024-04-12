from datetime import date

from sqlalchemy import Date, Enum, Index, LargeBinary, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.db import Base

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    phone: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))

    __table_args__ = (
        UniqueConstraint("email"),
        Index("idx_email", "email", unique=True),
    )