
class TestBookPastCompetition:

    def test_book_past_competition(self, client, competitions):
        response = client.get(f"/book/{competitions[1]['name']}/Iron%20Temple")
        assert response.status_code == 400
        assert "You cannot book places for the past competitions. This Competition held on" in response.data.decode()
        

    def test_book_future_competition(self, client, competitions):
        response = client.get(f"/book/{competitions[0]['name']}/Iron%20Temple")
        assert response.status_code == 200
        assert "Places available:" in response.data.decode()
        
