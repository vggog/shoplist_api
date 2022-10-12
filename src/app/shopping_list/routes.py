from fastapi import APIRouter


shopping_list_route = APIRouter(
    tags=['shopping_list']
)


@shopping_list_route.get(
    '/shopping-list-name={shopping_list_name}/all-items',
)
async def all_items_in_shopping_list(
    shopping_list_name: str,
):
    """
    Send all items in shopping list.
    """
    ...


@shopping_list_route.get(
    '/shopping-list-name={shopping_list_name}/create'
)
async def create_shopping_list(
    shopping_list_name: str,
):
    """
    Create shopping list.
    """
    ...


@shopping_list_route.post(
    '/shopping-list-name={shopping_list_name}/add-item',
)
async def add_item_in_shopping_list(
    shopping_list_name: str,
):
    """
    Add item in shopping list.
    """
    ...


@shopping_list_route.put(
    '/shopping-list-name={shopping_list_name}/edit-item',
)
async def edit_item_in_shopping_list(
    shopping_list_name: str,
):
    """
    Edit item in shopping list.
    """
    ...


@shopping_list_route.delete(
    '/shopping-list-name={shopping_list_name}/delete-item'
)
async def delete_item_in_shopping_list(
    shopping_list_name: str,
):
    """
    Delete item in shopping list.
    """
    ...


@shopping_list_route.get(
    '/shopping-list-name={shopping_list_name}/list-item={list_item}'
)
async def get_item_in_shopping_list(
    shopping_list_name: str,
    list_item: str
):
    """
    Get item in shopping list.
    """
    ...
