import app.core.db as db
import app.repositories.user_repository as user_repo
from app.exceptions import (
    EntityAlreadyExistsException,
    EntityNotFoundException,
)
from app.models.user import User
from app.schemas.user_schema import (
    UserCreateSchema,
    UserRole,
    UserSchema,
)

def create(dto: UserCreateSchema) -> UserSchema:
    user = User(**dto.model_dump())

    with db.create_session() as session:
        if user_repo.get_by_email(session, dto.email) is not None:
            raise EntityAlreadyExistsException("User with this email already exists")

        user = user_repo.save(session, user)

        return UserSchema.model_validate(user)


def get_all(role: UserRole | None) -> list[UserSchema]:
    with db.create_session() as session:
        users = user_repo.get_all(session, role)
        return list(map(UserSchema.model_validate, users))

def get_by_id(user_id: int) -> UserSchema:
    with db.create_session() as session:
        user = user_repo.get_by_id(session, user_id)
        if user is None:
            raise EntityNotFoundException("User not found")
        return UserSchema.model_validate(user)

def get_by_email(email: str) -> UserSchema:
    with db.create_session() as session:
        user = user_repo.get_by_email(session, email)
        if user is None:
            raise EntityNotFoundException("User not found")
        return UserSchema.model_validate(user)

def delete(user_id: int) -> None:
    with db.create_session() as session:
        user = user_repo.get_by_id(session, user_id)
        if user is None:
            raise EntityNotFoundException("User not found")
        user_repo.delete(session, user)

def check_credentials(email: str) -> bool:
    with db.create_session() as session:
        user = user_repo.get_by_email(session, email)
        if user is None:
            return False

        return True