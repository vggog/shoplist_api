from src.core.base.services import BaseService
from src.app.shopping_list.repositories import ShoppingListRepository


class ShoppingListService(BaseService):
    _repository = ShoppingListRepository()
