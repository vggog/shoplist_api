from abc import ABC

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.core.config import config
from src.core.base.models import BaseModel


class BaseRepository(ABC):
    _model: type[BaseModel] = NotImplemented

    def create(self, **data_for_create):
        created_object = self._model(**data_for_create)
        engine = create_engine(config.DB_URL)

        with Session(engine) as session:
            session.add(created_object)
            session.commit()

        return created_object
