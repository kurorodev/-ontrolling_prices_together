from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core import db
from app.core.settings import settings
from app.exceptions import EntityAlreadyExistsException
from app.routers.status import router as get_status
from app.routers.shop import router as shop_router
from app.routers.user import router as user_router
from app.routers.photo import router as photo_router
#from app.services import user_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.initialize()

    if settings.initial_user_schema is not None:
        try:
            user_service.create(settings.initial_user_schema)
        except EntityAlreadyExistsException:
            print("Initial user already exist. Skipping.")

    yield

    db.release()

def create_app():
    app = FastAPI(redoc_url=None, title="Controlling prices together 2024", lifespan=lifespan)

    app.include_router(get_status)
    app.include_router(user_router)
    app.include_router(photo_router)
    app.include_router(shop_router)

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app