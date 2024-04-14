# from typing import Annotated

# from fastapi import APIRouter, Depends

# import app.services.shop_service as shop_service
# from app.models.shop import Shop
# from app.schemas.shop_schema import (
#     ShopSchema,
#     ShopCreateSchema
# )
# from app.schemas.user_schema import (UserRole)
# from app.security import authenticate, require_admin

# router = APIRouter(prefix="/shops", tags=["Shop"])


# @router.post("/create", response_model=ShopSchema)
# def create_shop(shop: ShopCreateSchema):
#     return shop_service.create(shop)

# @router.get("/", response_model=list[ShopSchema])
# def get_all_shops(role: UserRole | None = None):
#     return shop_service.get_all(role)

# @router.get("/current", response_model=ShopSchema)
# def get_current_shop(shop: Annotated[Shop]):
#     return ShopSchema.model_validate(shop)

# @router.get(
#     "/{user_id}", response_model=ShopSchema
# )
# def get_shop_by_id(shop_id: int):
#     return shop_service.get_by_id(shop_id)

# @router.delete("/{user_id}")
# def delete_shop(shop_id: int):
#     return shop_service.delete(shop_id)