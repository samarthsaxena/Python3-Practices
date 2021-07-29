from locust import User, task, constant
from six import print_


class MyTest(User):
    wait_time = constant(1)

    @task
    def say_hello(self):
        print("Hello !")
        
    @task
    def wear_mask(self):
        print("wear mask")

    @task
    def say_goodbye(self):
        print("goodbye!")
        
