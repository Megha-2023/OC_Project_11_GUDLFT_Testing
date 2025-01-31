import pytest
from server import create_app

@pytest.fixture
def client(competitions, clubs):
    app = create_app({"TESTING": True}, competitions=competitions, clubs=clubs)
    with app.test_client() as client:
        yield client

<<<<<<< HEAD
=======
@pytest.fixture
def competitions():
    return [
        {
            "name": "Fall Classic",
            "numberOfPlaces": "13"
        }
    ]
>>>>>>> bugfix/points_not_updated

@pytest.fixture
def clubs():
    return [
        {
            "name": "She Lifts",
<<<<<<< HEAD
            "email": "kate@shelifts.co.uk",
            "points": "12"
        }
    ]

=======
            "points": "10"
        }
    ]
>>>>>>> bugfix/points_not_updated
