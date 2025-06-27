# LambdaTest_Selenium 101
This Assignment demonstrates 3 test scenarios using Selenium and Python's pytest framework. The test scenarios involve automating interactions with the LambdaTest Selenium Playground.

## Table Of Contents

* [Pre-requisites](#pre-requisites)
* [Setting Up Your Authentication](#Setting-Up-Your-Authenticationt)
* [Executing The Test](#Executing-The-Test)

## Prerequisites

Before you can start performing **Python** automation testing with **Selenium**, you would need to:

* Install the latest Python build from the [official website](https://www.python.org/downloads/). We recommend using the latest version.
* Make sure **pip** is installed in your system. You can install **pip** from [here](https://pip.pypa.io/en/stable/installation/).
* Download the latest **Selenium Client** and its **WebDriver bindings** from the [official website](https://www.selenium.dev/downloads/). Latest versions of **Selenium Client** and **WebDriver** are ideal for running your automation script on LambdaTest Selenium cloud grid.

### Installing Selenium Dependencies And Tutorial Repo

**Step 1:** Clone the LambdaTest’s LambdaTest_SeleniumPyhton101 repository and navigate to the code directory as shown below:

```bash
git clone https://github.com/PriyankaPothamsetty/LambdaTest_SeleniumPython101.git
cd LambdaTest_SeleniumPython101
```

**Step 2:** Download the driver from the link, or you can use **pip** to install it.
```bash
pip install -r requirements.txt
export PYTHONWARNINGS="ignore:Unverified HTTPS request"   //Disable ssl warning
```

### Setting Up Your Authentication

Make sure you have your LambdaTest credentials with you to run test automation scripts. You can get these credentials from the [LambdaTest Automation Dashboard]
Before running the tests, update the following variables in the code:

**Step 2:** 
Set LambdaTest **Username** and **Access Key** in ``` testdata.py.```

### Executing The Test

**Step 3:** You would need to execute the below command in your terminal/cmd.

```bash
cd LambdaTest_SeleniumPyhton101

python -m pytest ./tests

or

python -m pytest -n 2 ./tests
```

Your test results would be displayed on the test console (or command-line interface if you are using terminal/cmd) and on LambdaTest automation dashboard. 


