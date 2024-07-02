import pytest
from selenium import webdriver
from base.webdriverFact import webdriverfactory

@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = webdriverfactory(browser)
    driver = wdf.GetWebDriverInstance()

    # if browser == 'firefox':
    #     url = "https://www.letskodeit.com/"
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     print("Running tests on FF")
    #     driver.get(url)
    # else:
    #     url = "https://www.letskodeit.com/"
    #     driver = webdriver.Chrome()
    #     driver.get(url)
    #     print("Running tests on chrome")


    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")