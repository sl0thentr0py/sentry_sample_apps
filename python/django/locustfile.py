from locust import HttpUser, task

class User(HttpUser):
    @task
    def scope1(self):
        self.client.get("/scope1")

    @task
    def scope2(self):
        self.client.get("/scope2")
