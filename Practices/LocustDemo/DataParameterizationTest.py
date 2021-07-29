from locust import SequentialTaskSet, HttpUser, constant, task
from readcsvfile import CsvRead

class ParameterizedTests(SequentialTaskSet):

    @task
    def place_order(self):
        test_data = CsvRead("customer-data.csv").read()
        print(test_data)

        data = {
            "custname": test_data['name'],
            "custemail": test_data['email'],
            "size": test_data['size'],
            "toppings": test_data['toppings'],
            "delivery": test_data['time'],
            "comments": test_data['instructions']
        }

        name = "Order for "+ test_data['name']

        with self.client.post("/post", catch_response = True, name = name, data=data) as res:
            if res.status_code == 200 and test_data['name'] in res.text:
                res.success()
            else:
                res.failure("Failure while processing this order")


class TestParameterizedLoad(HttpUser):
    wait_time = constant(1)
    host = "https://httpbin.org"
    tasks = [ParameterizedTests]
