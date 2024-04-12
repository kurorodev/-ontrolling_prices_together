from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.db import Base

class Shop(Base):
    __tablename__ = "shop"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    shop_name: Mapped[str] = mapped_column(String(50))
    adress: Mapped[str] = mapped_column(String(50))