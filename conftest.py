from selenium import webdriver
import pytest
from utilities.Test_Data import Test_Data

@pytest.fixture(params=["chrome","firefox","edge"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
    request.cls.driver = driver
    print("Browser :" ,request.param)
    driver.get(Test_Data.url)
    driver.maximize_window()
    yield
    print("Close driver")
    driver.close()