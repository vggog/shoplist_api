import sqlalchemy as sa

from src.core.base.models import BaseModel


class ShoppingList(BaseModel):
    __tablename__ = 'shopping_list'

    title = sa.Column(
        sa.String,
        nullable=False,
    )
    description = sa.Column(
        sa.String,
    )
