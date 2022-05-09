from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.2, 1)

    @task(1)
    def test1(self):
        self.client.get("/")
