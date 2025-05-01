
class TestPointsDisplay:

    def test_points_display_board(self, client):
        response = client.get("/")
        assert response.status_code == 200
        assert "Clubs Details" in response.data.decode()
    
