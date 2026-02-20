"""
1. For common fixtures shared by multiple files regarding execute test cases we write fixture in the conftest file
2. Suppose you have requirement that after run setup fixture in conftest you just want to run all methods
under class TestExample & finally run method after yield keyword.
For that we have to add 'scope = "class"' in @pytest.fixture(scope='class') in conftest file. This is for class level operation.
If mentioned nothing inside @pytest.fixture() it will be method level operation.
3. If we want cross browser test we have to mention them in markers 'params' (called parameterize) i.e. '@pytest.fixture(params=["Firefox","Chrome", "Opera"])'
request object will pick individual param value & return in 'request.param'.
That returned crossBrowser fixture value will be passed to 'test_crossBrowser' method in 'test_demo1' & print each value.
"""

import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

#**During cross browser test we should mention local alias like chromeService, firefoxService otherwise Service will overwrite multiple times.

#register before run browser specific run commands in terminal
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="my option: type1 or type2")
#write "--browser_name" so it will pass the driver in register file
#write default="name of browser" you want to run in default without CLI commands. CLI command prioritize first.

@pytest.fixture(params=["chrome","firefox","edge"])  # for cross browser test & no CLI commands
#@pytest.fixture(scope="function")
def browserInstance(request):
    # browser_name = request.config.getoption("--browser_name")
    browser_name = request.param                       #each param passes here if match then execute
#getoption retrieves the --browser_name with key chrome or firefox or other browser & store it variable browser_name

#Firefox fails more as geckodriver is more strictly validated. Enterprise policies often restrict Firefox as driver path is necessary for local execution.
    if browser_name == "chrome":
        options = ChromeOptions()
        driver = webdriver.Remote(command_executor="http://chrome:4444/wd/hub",options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Remote(command_executor="http://firefox:4444/wd/hub",options=options)
    elif browser_name == "edge":
        options = EdgeOptions()
        driver = webdriver.Remote(command_executor="http://edge:4444/wd/hub",options=options)
    #elif browser_name == "safari":
    #     driver = webdriver.Safari() #safaridriver is built into macOS. Selenium auto-launches it. No executable path & Service Object is required.
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported. Only 'chrome' and 'safari' are enabled.")
    driver.implicitly_wait(5)
    yield driver
    time.sleep(20)
    driver.quit()
