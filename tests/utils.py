from sqlalchemy import create_engine

from src.core.config import config


def get_test_engine():
    """
    Return sqlalchemy engine for the test database
    """
    return create_engine(config.DB_URL_TEST)
