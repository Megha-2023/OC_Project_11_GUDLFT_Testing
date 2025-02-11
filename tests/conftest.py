import pytest
from server import create_app


@pytest.fixture
def client(competitions, clubs):
    app = create_app({"TESTING": True}, competitions=competitions, clubs=clubs)
    with app.test_client() as client:
        yield client


@pytest.fixture
def users():
    users = [
        {"email": ["admin@irontemple.com", "wrongemail@simplylift.co"]}
    ]
    return users


@pytest.fixture
def competitions():
    return [
        {
            "name": "Fall Classic",
            "date": "2025-10-22 13:30:00",
            "numberOfPlaces": "13"
        },
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        }
    ]

@pytest.fixture
def clubs():
    return [
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "10"
        }
    ]
