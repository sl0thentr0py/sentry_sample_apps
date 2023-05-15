from locust import HttpUser, task

class User(HttpUser):
    @task
    def celery_task(self):
        self.client.get("/celery_task")
