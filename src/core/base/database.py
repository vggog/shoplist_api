from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


class DBConnection:

    def __init__(self, db_url):
        self.db_url = db_url

    @staticmethod
    def get_sessionmaker(db_url: str) -> sessionmaker:
        engine = create_engine(db_url)
        return sessionmaker(engine)

    def get_session(self) -> Session:
        session = self.get_sessionmaker(self.db_url)
        return session()
