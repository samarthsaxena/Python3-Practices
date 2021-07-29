from locust import HttpUser, constant, SequentialTaskSet, task, log
import re
import random


class PetStore(SequentialTaskSet):

    def __int__(self, parent):
        super().__init__(parent)
        self.jsession = ""
        self.random_product = ""

    @task
    def home_page(self):
        with self.client.get("", catch_response=True, name="home_page") as response:
            if "Welcome to JPetStore" in response.text and response.elapsed.total_seconds() < 5.0:
                response.success()
                log.setup_logging("Testing")
            else:
                response.failure("Home page took more than 2 Seconds to load.")

    @task
    def enter_store(self):
        products = ['Fish', 'Dogs', 'Cats', 'Reptiles', 'Birds']
        with self.client.get("/actions/Catalog.action", catch_response=True, name="enter_store") as response:
            for product in products:
                if product in response.text:
                    response.success()
                else:
                    response.failure("Product check failed.")
                    break

            try:
                jsession = re.search(r"jsession=(.+?)\?", response.text)  # extract jsession id
                self.jsession = jsession.group(1)
            except AttributeError:
                self.jsession = ""

    @task
    def signin_page(self):

        self.client.cookies.clear()  # Start with clean state
        url = "/actions/Account.action;jsession=" + self.jsession + "?signonForm="
        with self.client.get(url, catch_response=True, name="signin_page") as response:
            if "Please enter your username and password" in response.text:
                response.success()
            else:
                response.failure("Signin page check failed.")

    @task
    def login(self):

        self.client.cookies.clear()
        url = "/actions/Account.action"
        data = {
            "username": "someuser1",
            "password": "passowrd1",
            "signin": "Login"
        }

        with self.client.post(url, data=data, catch_response=True, name="login ") as response:
            print(response.text)
            if "Welcome ABC!" in response.text:
                response.success()
                try:
                    random_product = re.findall(r"Catalog.action\?viewCatagory=&catagoryId=(.+?)\"",
                                                response.text)  # extracting all of the products
                    self.random_product = random.choice(random_product)
                except AttributeError:
                    self.random_product = ""
            else:
                response.failure("Sign in failed.")

    @task
    def random_product_page(self):
        url = "/actions/Catalog.action?viewCatagory=&catagoryId" + self.random_product
        name = "Test_" + self.random_product + "_Page"
        with self.client.get(url, catch_response=True, name=name) as response:
            if self.random_product in response.text:
                response.success()
            else:
                response.failure("Product page not loaded.")

    @task
    def sign_out(self):

        with self.client.get("/actions/Account.action?signoff=", name="Sign out", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Could not sign out.")
        self.client.cookies.clear()


class TestUserAuthenticationLoad(HttpUser):
    wait_time = constant(2)
    host = "https://petstore.octoperf.com"
    tasks = [PetStore]
