import pytest
from server import create_app

@pytest.fixture
def client(competitions, clubs):
    app = create_app({"TESTING": True}, competitions=competitions, clubs=clubs)
    with app.test_client() as client:
        yield client

@pytest.fixture
def competitions():
    return [
        {
            "name": "Fall Classic",
            "numberOfPlaces": "13"
        }
    ]

@pytest.fixture
def clubs():
    return [
        {
            "name": "She Lifts",
            "points": "10"
        }
    ]
