from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.edge.webdriver import WebDriver as Edge
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from pytest import fixture
from POM.homepage import Homepage
from POM.admin_loginpage import AdminLoginPage
from POM.admin_dashboardpage import AdminDashboardPage

import pytest



def pytest_html_report_title(report):
    """Set the title of the HTML report."""
    report.title = "My Custom Test Report"


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", dest="browser")
    parser.addoption("--env", action="store", default="test", dest="env")
    parser.addoption("--headless", action="store_true", dest="headless", default=False)

@fixture
def _config(request):
    class TestEnvironment:
        url = "http://49.249.28.218:8081/AppServer/Hospital_Management_System/index.html"
        username = "admin"
        password = "Test@12345"

    class StageEnvironment:
        url = "http://49.249.28.218:8081/AppServer/Hospital_Management_System/index.html"
        username = "admin"
        password = "Test@12345"

    exc_env = request.config.option.env

    if exc_env.upper() == "TEST":
        return TestEnvironment()
    elif exc_env.upper() == "STAGE":
        return StageEnvironment()
    else:
        raise Exception("invalid environment")

@fixture
def driver(_config,request):
    browser_name = request.config.option.browser
    is_headless = request.config.option.headless
    options = None

    if browser_name.upper() == "CHROME":
        if is_headless:
            options = ChromeOptions()
            options.add_argument("--headless=new")
        _driver = Chrome(options=options)

    elif browser_name.upper() == "FIREFOX":
        if is_headless:
            options = FirefoxOptions()
            options.add_argument("--headless")
        _driver = Firefox(options=options)

    elif browser_name.upper() == "EDGE":
        if is_headless:
            options = EdgeOptions()
            options.add_argument("--headless=new")
        _driver = Edge(options=options)

    else:
        raise Exception("Invalid browser")
    _driver.get(_config.url)
    _driver.maximize_window()
    yield _driver
    _driver.quit()

@fixture
def pages(driver):
  class Pages:
      homepage = Homepage(driver)
      admin_loginpage = AdminLoginPage(driver)
      admin_dashbordpage = AdminDashboardPage(driver)

  return Pages

