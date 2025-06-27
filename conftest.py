from selenium import webdriver
import pytest
from utilities.Test_Data import Test_Data
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.ie.options import Options as IEOptions
from selenium.webdriver.remote.remote_connection import RemoteConnection, ClientConfig
import warnings
from os import environ
from selenium.common import JavascriptException

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
    driver.get(Test_Data.url_login)
    driver.maximize_window()
    yield
    print("Close driver")
    driver.close()

#1st setp : declare variables for setting up LambdaTest
user_name = "priyankapothamsetty"
access_token = "LT_hoQsTu0nmHmQKmpqPyhtxa5ZrZCFFt8C0FYxwxLUwoyCjGJ"
#LT_hoQsTu0nmHmQKmpqPyhtxa5ZrZCFFt8C0FYxwxLUwoyCjGJ
remotly_url = "https://" + user_name + ":" + access_token + "@hub.lambdatest.com/wd/hub"

# 2nd step : Define The Dasired capabilities(3 caps)
def suppress_resource_warnings():
    warnings.filterwarnings("ignore", category=UserWarning)

@pytest.fixture(scope='function', params=['chrome', "firefox", "edge"])
def setup_teardown(request):
    """
    Initialize Driver for Selenium Grid On LambdaTest
    :param request:
    :return:
    """
    # Desired capabilities for Chrome on LambdaTest
    chrome_caps = {
        "build": environ.get("BUILD", "Chrome Selenium 101"),
        "project": "LambdaTest Selenium 101",
        "name": request.node.name,
        "browserName": "Chrome",
        "browserVersion": "88.0",
        "platformName": "Windows 10",
        "user_name": user_name,
        "access_token": access_token,
        "visual": True,
        "video": True,
        "network": True,
        "console": True,
        "w3c": True,
        "plugin": "python-pytest"
    }
    # Desired capabilities for Firefox on LambdaTest
    firefox_caps = {
        "build": environ.get("BUILD", "Firefox Selenium 101"),
        "project": "LambdaTest Selenium 101",
        "name": request.node.name,
        "browserName": "Firefox",
        "browserVersion": "82.0",
        "platformName": "Windows 7",
        "user_name": user_name,
        "access_token": access_token,
        "visual": True,
        "video": True,
        "network": True,
        "console": True,
        "w3c": True,
        "plugin": "python-pytest"
    }

    # Desired capabilities for Edge on LambdaTest
    edge_caps = {
        "build": environ.get("BUILD", "Edge Selenium 101"),
        "project": "LambdaTest Selenium  101",
        "name": request.node.name,
        "browserName": "MicrosoftEdge",
        "browserVersion": "87.0",
        "platformName": "macOS Sierra",
        "user_name": user_name,
        "access_token": access_token,
        "network": True,
        "visual": True,
        "video": True,
        "console": True,
        "w3c": True,
        "plugin": "python-pytest"
    }

   
    # Initialize the WebDriver based on the browser parameter
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.set_capability("LT:Options", chrome_caps)
        config = ClientConfig(remote_server_addr=remotly_url)
        command_executor = RemoteConnection(client_config=config)
        suppress_resource_warnings()
        driver = webdriver.Remote(
            command_executor=command_executor,
            options=chrome_options
        )

    elif request.param == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.set_capability("LT:Options", firefox_caps)
        config = ClientConfig(remote_server_addr=remotly_url)
        command_executor = RemoteConnection(client_config=config)
        suppress_resource_warnings()
        driver = webdriver.Remote(
            command_executor=command_executor,
            options=firefox_options
        )
    elif request.param == "edge":
        edge_options = EdgeOptions()
        edge_options.set_capability("LT:Options", edge_caps)
        config = ClientConfig(remote_server_addr=remotly_url)
        command_executor = RemoteConnection(client_config=config)
        suppress_resource_warnings()
        driver = webdriver.Remote(
            command_executor=command_executor,
            options=edge_options
        )
    

    # Assign the driver to the test class
    request.cls.driver = driver
    print(f"Browser: {request.param}")



    # Navigate to the specified URL and maximize the window
    driver.get(Test_Data.url_login)
    driver.maximize_window()

    # Yield the driver for use in tests
    yield driver

    # Quit the driver after tests are done
    print("closing...")
    driver.quit()

def change_test_status(driver, flag):

    try:
        if flag:
            driver.execute_script("lambda-status=passed")
        else:
            driver.execute_script("lambda-status=failed")

    except JavascriptException:
        pass
