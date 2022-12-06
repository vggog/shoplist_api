from fastapi.testclient import TestClient
from starlette import status

from src.main import app


def test_shopping_list_create_success():
    """Success create shopping list"""
    client = TestClient(app)
    url = app.url_path_for('create_shopping_list')
    response = client.post(
        url,
        json={
            'title': 'Testing shopping list',
            'description': 'Description for shopping list',
        },
    )

    assert response.status_code == status.HTTP_201_CREATED
