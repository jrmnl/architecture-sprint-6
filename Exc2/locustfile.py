from locust import FastHttpUser, between, task

class WebsiteUser(FastHttpUser):
    wait_time = between(1, 5)

    @task
    def index(self):
        self.client.client.clientpool.close() # self.client.client is not a typo
        response = self.client.get("/")
