from pydantic import BaseModel
from typing_extensions import Annotated

class PhotoSchema(BaseModel):
    file_bytes: Annotated(str)