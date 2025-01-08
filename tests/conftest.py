import pytest
from server import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client

@pytest.fixture
def users():
    users = [
        {"email": ["john@simplylift.co", "wrongemail@simplylift.co"]}
    ]
    return users
