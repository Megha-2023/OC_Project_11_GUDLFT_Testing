import pytest
from server import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client

@pytest.fixture
def competitions():
    return [
        {
            "competition": "Fall Classic",
            "numberOfPlaces": "13"
        }
    ]

@pytest.fixture
def clubs():
    return [
        {
            "name": "She Lifts",
            "points": "12"
        }
    ]