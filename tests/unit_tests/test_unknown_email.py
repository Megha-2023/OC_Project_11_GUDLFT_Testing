class TestUnknownEmail:

    def test_correct_email(self, client, users):
        response = client.post('/showSummary', data={"email": users[0]['email'][0]})
        assert response.status_code == 200
        assert "Welcome" in response.data.decode()


    def test_unknown_email(self, client, users):
        response = client.post('/showSummary', data={"email": users[0]['email'][1]})
        assert response.status_code == 404
        assert "Oops Sorry! The email was not found." in response.data.decode()