import sqlalchemy as sa

from src.core.base.models import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    username = sa.Column(
        sa.String,
        nullable=False,
    )
    email = sa.Column(
        sa.String,
        nullable=False,
    )
    password = sa.Column(
        sa.String,
        nullable=False,
    )
