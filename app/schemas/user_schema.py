from datetime import date
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing_extensions import Annotated


class UserRole(StrEnum):
    ADMIN = "ADMIN"
    USER = "USER"

class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: Annotated[str, Field(max_length=50)]
    second_name: Annotated[str, Field(max_length=50)]
    phone: Annotated[str, Field(max_length=50)]
    email: EmailStr
    role: UserRole

class UserCreateSchema(BaseModel):

    first_name: Annotated[str, Field(max_length=50)]
    second_name: Annotated[str, Field(max_length=50)]
    phone: Annotated[str, Field(max_length=50)]
    email: EmailStr
    role: UserRole
