from datetime import date

from sqlalchemy import Date, Enum, Index, LargeBinary, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date

from sqlalchemy import Date, Enum, Index, LargeBinary, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app import config
from app.core.db import Base

class Shop(Base):
    __tablename__ = "shop"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    shop_name: Mapped[str] = mapped_column(String(50))
    shop_adress: Mapped[str] = mapped_column(String(50))

    if_written: Mapped[bool] = mapped_column(default=False)