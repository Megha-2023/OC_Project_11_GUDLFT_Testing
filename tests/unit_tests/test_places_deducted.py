

class TestPlacesDeducted:
    def test_places_deducted_correctly(self, client, competitions, clubs):
        
        initial_places = int(competitions[0]["numberOfPlaces"])

        response = client.post("/purchasePlaces", data={
            "competition": competitions[0]["name"],
            "club": clubs[0]["name"],
            "places": "5"
        })

        updated_places = int(competitions[0]["numberOfPlaces"])
        assert response.status_code == 200
        assert b"Great-booking complete!" in response.data
        assert updated_places == initial_places - 5
