from locust import SequentialTaskSet, HttpUser, constant, task


class LoadReqRes(SequentialTaskSet):

    @task
    def get_users(self):
        res = self.client.get("/")
        print("Got status:", res.status_code)

    @task
    def post_users(self):
        res = self.client.post("/?status=success")
        print("Got status:", res.status_code)


class DemoSeqTaskTests(HttpUser):
    wait_time = constant(1)
    host = "http://example.com"
    tasks = [LoadReqRes]
