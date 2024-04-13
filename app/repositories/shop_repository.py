from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from app.models.shop import Shop
from app.models.user import User
from app.schemas.user_schema import UserRole

def get_all(session: Session, role: UserRole | None) -> list[Shop]:
    q = select(Shop)
    if role is not None:
        q = q.filter(User.role == role)
    q = q.order_by(Shop.id)

    return list(session.execute(q).scalars())


def get_by_id(session: Session, shop_id: int) -> Shop | None:
    return session.get(Shop, shop_id)

def get_by_name(session: Session, shop_name: str) -> Shop | None:
    q = select(Shop).where(Shop.shop_name == shop_name).limit(1)
    return session.execute(q).scalar_one_or_none()

def get_by_adress(session: Session, shop_adress: str) -> Shop | None:
    q = select(Shop).where(Shop.shop_adress == shop_adress).limit(1)
    return session.execute(q).scalar_one_or_none()

def get_check_by_id(session: Session, shop_id: int) -> bool | None:
    return session.get(Shop.if_written, shop_id)

def get_check_by_name(session: Session, shop_name: str) -> bool | None:
    q = select(Shop.if_written).where(Shop.shop_name == shop_name).limit(1)
    return session.execute(q).scalar_one_or_none()

def get_check_by_adress(session: Session, shop_adress: str) -> bool | None:
    q = select(Shop.if_written).where(Shop.shop_adress == shop_adress).limit(1)
    return session.execute(q).scalar_one_or_none()

def save(session: Session, shop: Shop) -> Shop:
    session.add(shop)
    session.flush()
    session.commit()
    return shop


def delete(session: Session, shop: Shop) -> None:
    session.delete(shop)
    session.commit()