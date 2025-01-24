
class TestBookMoreThan12Places:

    def test_book_12_places(self, client, competitions, clubs):
        initial_places = int(competitions[0]["numberOfPlaces"])
        response = client.post("/purchasePlaces", data={
            "competition": competitions[0]["name"],
            "club": clubs[0]["name"],
            "places": "9"
        })
        updated_places = int(competitions[0]["numberOfPlaces"])
        assert response.status_code == 200
        assert "Great-booking complete!" in response.data.decode()
        assert updated_places == initial_places - 9


    def test_book_more_than_12_places(self, client, competitions, clubs):
        initial_places = int(competitions[0]["numberOfPlaces"])
        response = client.post("/purchasePlaces", data={
            "competition": competitions[0]["name"],
            "club": clubs[0]["name"],
            "places": "15"
        })
        updated_places = int(competitions[0]["numberOfPlaces"])
        assert response.status_code == 400
        assert "You cannot book more than 12 places per competition" in response.data.decode()
        assert updated_places == initial_places
