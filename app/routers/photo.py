from fastapi import APIRouter, File
from typing import Annotated

router = APIRouter(prefix="/files", tags=["Files"])

@router.post("/check_price")
async def check_price(file: Annotated[bytes, File()]):
    return "Цена соответствует социальной цене"

@router.post("/check_socprice")
async def check_socprice(file: Annotated[bytes, File()]):
    return {"file_bytes": str(file)}