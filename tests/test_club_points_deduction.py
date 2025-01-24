
class TestClubPointsDeduction:

    def test_points_deducted_correct(self, client, competitions, clubs):
        response = client.post("/purchasePlaces", data={
            "competition": competitions[0]["competition"],
            "club": clubs[0]["name"],
            "places": "10"
        })
        assert response.status_code == 200
        assert "Great-booking complete!" in response.data.decode()

    def test_points_deducted_wrong(self, client, competitions, clubs):
        response = client.post("/purchasePlaces", data={
            "competition": competitions[0]["competition"],
            "club": clubs[0]["name"],
            "places": "13"
        })
        assert response.status_code == 400
        assert "You do not have enough points left to book the place." in response.data.decode()
