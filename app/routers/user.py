from typing import Annotated

from fastapi import APIRouter, Depends

import app.services.user_service as user_service
from app.models.user import User
from app.schemas.user_schema import (
    UserCreateSchema,
    UserSchema,
    UserRole
)
from app.security import authenticate, require_admin

router = APIRouter(prefix="/users", tags=["User"])


@router.post("/create", response_model=UserSchema)
def create_user(user: UserCreateSchema):
    return user_service.create(user)

@router.get("/", response_model=list[UserSchema])
def get_all_users(role: UserRole | None = None):
    return user_service.get_all(role)

@router.get("/current", response_model=UserSchema)
def get_current_user(user: Annotated[User, Depends(authenticate)]):
    return UserSchema.model_validate(user)

@router.get(
    "/{user_id}", response_model=UserSchema, dependencies=[Depends(require_admin)]
)
def get_user_by_id(user_id: int):
    return user_service.get_by_id(user_id)

@router.delete("/{user_id}", dependencies=[Depends(require_admin)])
def delete_user(user_id: int):
    return user_service.delete(user_id)