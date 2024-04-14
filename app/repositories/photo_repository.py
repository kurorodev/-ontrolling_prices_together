'''from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from app.models.photo import Photo

def save(session: Session, photo: Photo) -> Photo:
    session.add(photo)
    session.flush()
    session.commit()
    return user

def delete(session: Session, photo: Photo) -> None:
    session.delete(photo)
    session.commit()