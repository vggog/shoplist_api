from src.core.base.repositories import BaseRepository
from src.app.shopping_list.models import ShoppingList


class ShoppingListRepository(BaseRepository):
    _model = ShoppingList
