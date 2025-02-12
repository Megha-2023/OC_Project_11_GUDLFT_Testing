from locust import HttpUser, task, between
import time


class ProjectPerfTest(HttpUser):
    wait_time = between(1, 3)

    @task
    def test_load_competitions_time(self):
        start_time = time.time()
        response = self.client.get("/")
        end_time = time.time()

        assert response.status_code == 200
        assert (end_time - start_time) <= 5, "Competitions loading took long!"
    
    @task
    def login(self):
        response = self.client.post('/showSummary', {"email": "john@simplylift.co"})

