from fastapi import APIRouter, File
from typing import Annotated

router = APIRouter(prefix="/files", tags=["Files"])

@router.post("/upload")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_bytes": str(file)}