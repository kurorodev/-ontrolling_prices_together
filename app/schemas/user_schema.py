from datetime import date
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing_extensions import Annotated

class UserSchema(BaseModel):
    #model_config = ConfigDict(from_attributes=True)

    id: int
    phone: Annotated[str, Field(max_length=50)]
    email: EmailStr