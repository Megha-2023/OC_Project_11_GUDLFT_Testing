
class TestPointsUpdated:

    def test_points_updated_correct(self, client, competitions, clubs):
        initial_points = int(clubs[0]["points"])
        response = client.post("/purchasePlaces", data={
            "competition": competitions[0]["name"],
            "club": clubs[0]["name"],
            "places": "5"
        })
        updated_points = int(clubs[0]["points"])
        assert response.status_code == 200
        assert updated_points == initial_points - 5

    def test_points_not_updated_correct(self, client, competitions, clubs):
        initial_points = int(clubs[0]["points"])
        response = client.post("/purchasePlaces", data={
            "competition": competitions[0]["name"],
            "club": clubs[0]["name"],
            "places": "15"
        })
        updated_points = int(clubs[0]["points"])
        assert response.status_code == 400
        assert updated_points == initial_points
