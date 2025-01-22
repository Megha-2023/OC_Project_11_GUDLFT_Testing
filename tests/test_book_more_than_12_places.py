
class TestBookMoreThan12Places:

    def test_book_12_places(self, client, competitions, clubs):
        response = client.post("/purchasePlaces", data={
            "competition": competitions[0]["competition"],
            "club": clubs[0]["name"],
            "places": "10"
        })

        assert "Great-booking complete!" in response.data.decode()
        assert response.status_code == 200


    def test_book_more_than_12_places(self, client, competitions, clubs):
        response = client.post("/purchasePlaces", data={
            "competition": competitions[0]["competition"],
            "club": clubs[0]["name"],
            "places": "14"
        })

        assert "You cannot book more than 12 places per competition" in response.data.decode()
        assert response.status_code == 400
