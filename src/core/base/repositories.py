from sqlalchemy import select

from src.core.base.models import BaseModel
from src.core.database import DBConnection


class BaseRepository:
    model: type[BaseModel] = NotImplemented
    db_connection: DBConnection = NotImplemented

    async def get_object(self, **filters) -> model:
        statement = select(self.model).filter_by(**filters)

        with self.db_connection.get_session() as session:
            result = session.execute(statement)
            return result.unique().scalars().all()
