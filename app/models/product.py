from sqlalchemy import Date, Enum, Index, LargeBinary, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.db import Base

class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    soc_price: Mapped[bool] = mapped_column(default=False)
    price: Mapped[str] = mapped_column(String(10))
    product_name: Mapped[str] = mapped_column(String(50))


