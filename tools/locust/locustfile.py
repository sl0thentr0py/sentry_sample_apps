from random import randint

from locust import HttpUser, task

class RailsUser(HttpUser):
    @task(10)
    def success(self):
        self.client.get(f"/transaction/{randint(1, 100)}")

    @task
    def bork(self):
        self.client.get("/bork")
