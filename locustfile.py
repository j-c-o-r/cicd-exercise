from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(5, 15)

    @task(1)
    def test1(self):
        self.client.get("http://https://flask-exercise-service.azurewebsites.net")

    @task(2)
    def test2(self):
        self.client.post("https://flask-exercise-service.azurewebsites.net/predict")
