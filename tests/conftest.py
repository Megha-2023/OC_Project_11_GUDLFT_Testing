import pytest
from datetime import datetime, timedelta
from server import create_app


@pytest.fixture
def client(competitions, clubs):
    app = create_app({"TESTING": True}, competitions=competitions, clubs=clubs)
    with app.test_client() as client:
        yield client


@pytest.fixture
def clubs():
    return [
        {
            "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "12"
        }
    ]

