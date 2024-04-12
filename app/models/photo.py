from datetime import date

from sqlalchemy import Date, Enum, Index, LargeBinary, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date

from sqlalchemy import Date, Enum, Index, LargeBinary, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app import config
from app.core.db import Base

class Photo(Base):
    __tablename__ = "photo"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    file_bytes: Mapped[str] = mapped_column(String())

