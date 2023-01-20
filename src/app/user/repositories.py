from sqlalchemy.orm.session import Session

from src.core.base.repositories import BaseRepository
from src.app.user.models import UserModel
from src.core.base.database import DBConnection
from src.core.config import config


class UserRepository(BaseRepository):
    model: UserModel = UserModel
    db_connection: Session = DBConnection(config.DB_URL)
