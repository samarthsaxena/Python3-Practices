from locust import HttpUser, constant, SequentialTaskSet, task, log
import re
import random

class IDPAuthnTests(SequentialTaskSet):

    def __int__(self, parent):
        super().__init__(parent)
        self.jsession = ""

    @task
    def nidp_portal(self):
        with self.client.get("", catch_response=True, name="User login page") as response:
            print("Got response:",response.text)
            print("Got response code:", response.status_code)
            if "login" in response.text and response.elapsed.total_seconds() < 10.0:
                response.success()
                log.setup_logging("Testing")
            else:
                response.failure("Home page took more than 2 Seconds to load.")


class TestUserAuthenticationLoad(HttpUser):
    wait_time = constant(2)
    host = "https://node1.cluster.local:8443/nidp"
    tasks = [IDPAuthnTests]
