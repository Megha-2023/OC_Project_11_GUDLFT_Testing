
class TestBookingWithinPointsLimit:

    def test_booking_places_within_points_limit(self, client, competitions, clubs):
        response = client.post("/purchasePlaces", data={
            "competition": competitions[0]["name"],
            "club": clubs[0]["name"],
            "places": "5"
        })
        assert response.status_code == 200
        assert "Great-booking complete!" in response.data.decode()

    def test_booking_places_out_of_points_limit(self, client, competitions, clubs):
        response = client.post("/purchasePlaces", data={
            "competition": competitions[1]["name"],
            "club": clubs[0]["name"],
            "places": "11"
        })
        assert response.status_code == 400
        assert "You do not have enough points left to book the place. Points available:" in response.data.decode()
