'''import app.core.db as db
import app.repositories.photo_repository as photo_repo
from app.exceptions import (
    EntityAlreadyExistsException,
    EntityNotFoundException,
)

def create(dto: PhotoSchema) -> PhotoSchema:
    photo = Photo(**dto.model_dump())

    with db.create_session() as session:
        photo = photo_repo.save(session, photo)

        return PhotoSchema.model_validate(photo)'''