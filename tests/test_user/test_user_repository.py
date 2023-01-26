import pytest

from src.app.user.repositories import UserRepository
from src.core.base.database import DBConnection
from src.core.base.models import BaseModel
from src.core.config import config

from tests.factories import UserFactory
from tests.utils import get_test_engine


def setup():
    """
    Creates the desired database structure.
    """
    BaseModel.metadata.create_all(get_test_engine())


def teardown():
    """
    Delete database structure.
    """
    BaseModel.metadata.drop_all(get_test_engine())


@pytest.mark.asyncio
async def test_email_get_user():
    repository: UserRepository = UserRepository()
    repository.db_connection = DBConnection(config.DB_URL_TEST)

    db_connection = DBConnection(config.DB_URL_TEST)

    email = 'monobrow@igral.ru'
    user_factory = UserFactory()
    user = user_factory.get_user(username='fsdfs', email=email)

    with db_connection.get_session() as session:
        session.add(user)
        session.commit()

    assert await repository.get_object(email=email)


@pytest.mark.asyncio
async def test_email_get_user_not_found():
    repository: UserRepository = UserRepository()
    repository.db_connection = DBConnection(config.DB_URL_TEST)

    user = await repository.get_object(email='papamojet@my.tv')

    assert not user
