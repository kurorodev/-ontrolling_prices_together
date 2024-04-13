from datetime import date
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing_extensions import Annotated
class ShopSchema(BaseModel):

    id: int
    shop_name: Annotated[str, Field(max_length=50)]
    shop_adress: Annotated[str, Field(max_length=50)]
    if_written: bool

class ShopCreateSchema(BaseModel):

    shop_name: Annotated[str, Field(max_length=50)]
    shop_adress: Annotated[str, Field(max_length=50)]
    if_written: bool