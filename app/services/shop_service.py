# '''import app.core.db as db
# import app.repositories.shop_repository as shop_repo
# from app.exceptions import (
#     EntityAlreadyExistsException,
#     EntityNotFoundException,
# )
# from app.models.shop import Shop
# from app.schemas.user_schema import (
#     UserRole
# )
# from app.schemas.shop_schema import (ShopCreateSchema, ShopSchema)

# def create(dto: ShopCreateSchema) -> ShopSchema:
#     shop = Shop(**dto.model_dump())

#     with db.create_session() as session:
#         if shop.get_by_name(session, dto.shop_name) is not None:
#             raise EntityAlreadyExistsException("User with this name already exists")

#         shop = shop_repo.save(session, shop)

#         return ShopSchema.model_validate(shop)


# def get_all(role: UserRole | None) -> list[ShopSchema]:
#     with db.create_session() as session:
#         shops = shop_repo.get_all(session, role)
#         return list(map(ShopSchema.model_validate, shops))

# def get_by_id(shop_id: int) -> ShopSchema:
#     with db.create_session() as session:
#         shop = shop_repo.get_by_id(session, shop_id)
#         if shop is None:
#             raise EntityNotFoundException("Shop not found")
#         return ShopSchema.model_validate(shop)

# def get_by_name(shop_name: str) -> ShopSchema:
#     with db.create_session() as session:
#         shop = shop_repo.get_by_email(session, shop_name)
#         if shop is None:
#             raise EntityNotFoundException("Shop not found")
#         return ShopSchema.model_validate(shop)
    
# def get_by_adress(shop_adress: str) -> ShopSchema:
#     with db.create_session() as session:
#         shop = shop_repo.get_by_email(session, shop_adress)
#         if shop is None:
#             raise EntityNotFoundException("Shop not found")
#         return ShopSchema.model_validate(shop)
    
# def get_check_by_id(shop_id: int) -> bool:
#     with db.create_session() as session:
#         written = shop_repo.get_check_by_id(session, shop_id)
#         return written

# def get_check_by_name(shop_name: str) -> bool:
#     with db.create_session() as session:
#         written = shop_repo.get_check_by_email(session, shop_name)
#         return written
    
# def get_check_by_adress(shop_adress: str) -> bool:
#     with db.create_session() as session:
#         written = shop_repo.get_check_by_email(session, shop_adress)
#         return written

# def delete(shop_id: int) -> None:
#     with db.create_session() as session:
#         shop = shop_repo.get_by_id(session, shop_id)
#         if user is None:
#             raise EntityNotFoundException("Shop not found")
#         user_repo.delete(session, shop)'''