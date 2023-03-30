from locust import HttpUser, task

class RailsUser(HttpUser):
    @task
    def success(self):
        self.client.get("/success")
        with self.client.get("/success", catch_response=True) as response:
            if response.text != "success":
                response.failure("Got wrong response")
