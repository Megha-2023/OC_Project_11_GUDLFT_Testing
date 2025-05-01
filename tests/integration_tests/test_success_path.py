
def test_index_page(client):
    """ Test loading of index page"""

    response = client.get('/')
    assert response.status_code == 200
    assert "Welcome to the GUDLFT Registration Portal!" in response.data.decode()


def test_successful_login(client, users):
    """ Test successful login with valid credentials"""

    response = client.post('/showSummary', data={"email": users[0]['email'][0]})
    assert response.status_code == 200
    assert "Welcome" in response.data.decode()


def test_book_upcoming_competition(client, competitions):
    """ Test booking only upcoming competition """

    response = client.get(f"/book/{competitions[0]['name']}/Iron%20Temple")
    assert response.status_code == 200
    assert "Places available:" in response.data.decode()


def test_purchase_place_update_points(client, competitions, clubs):
    """ Test booking no more than 12 places and club points updated correctly """

    initial_points = int(clubs[0]["points"])
    initial_places = int(competitions[0]["numberOfPlaces"])
    response = client.post("/purchasePlaces", data={
        "competition": competitions[0]["name"],
        "club": clubs[0]["name"],
        "places": "10"
    })
    updated_points = int(clubs[0]["points"])
    updated_places = int(competitions[0]["numberOfPlaces"])

    assert response.status_code == 200
    assert "Great-booking complete!" in response.data.decode()
    assert updated_points == initial_points - 10
    assert updated_places == initial_places - 10


def test_logout(client):
    """ Test logout link"""

    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
