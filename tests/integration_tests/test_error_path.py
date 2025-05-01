
def test_unsuccessful_login(client, users):
    """ Test login for invalid credentials"""

    response = client.post('/showSummary', data={"email": users[0]['email'][1]})
    assert response.status_code == 404
    assert "Oops Sorry! The email was not found." in response.data.decode()


def test_booking_past_cometition(client, competitions):
    """ Test booking past competition """

    response = client.get(f"/book/{competitions[1]['name']}/Iron%20Temple")
    assert response.status_code == 400
    assert "You cannot book places for the past competitions. This Competition held on" in response.data.decode()


def test_booking_more_than_12_places(client, competitions, clubs):
    """ Test booking more places than 12 per competition"""

    initial_places = int(competitions[0]["numberOfPlaces"])
    response = client.post("/purchasePlaces", data={
        "competition": competitions[0]["name"],
        "club": clubs[0]["name"],
        "places": "16"
    })
    updated_places = int(competitions[0]["numberOfPlaces"])
    assert response.status_code == 400
    assert "You cannot book more than 12 places per competition" in response.data.decode()
    assert updated_places == initial_places


def test_bookin_more_than_available_points(client, competitions, clubs):
    response = client.post("/purchasePlaces", data={
            "competition": competitions[1]["name"],
            "club": clubs[0]["name"],
            "places": "11"
        })
    assert response.status_code == 400
    assert "You do not have enough points left to book the place. Points available:" in response.data.decode()
