
class TestBookPastCompetition:

    def test_book_past_competition(self, client):
        response = client.get('/book/Spring%20Festival/Simply%20Lift')
        assert "You cannot book places for the past competitions." in response.data.decode()
        assert response.status_code == 400


    def test_book_future_competition(self, client):
        response = client.get('/book/Fall%20Classic/Simply%20Lift')
        assert "Places available" in response.data.decode()
        assert response.status_code == 200
