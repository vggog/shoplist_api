import sqlalchemy as sa

from src.core.base.models import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'users'

    username = sa.Column(
        sa.String,
        unique=True,
    )
    name = sa.Column(
        sa.String,
    )
    surname = sa.Column(
        sa.String,
    )
    email = sa.Column(
        sa.String,
    )
    phone_number = sa.Column(
        sa.String,
    )
