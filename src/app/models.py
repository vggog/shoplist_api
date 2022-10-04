import sqlalchemy

from src.core.base.models import BaseModel


class ShoppingList(BaseModel):
    __tablename__ = 'shopping_list'

    title = sqlalchemy.Column(
        sqlalchemy.String,
        nulable=False,
    )
    description = sqlalchemy.Column(
        sqlalchemy.String,
    )
