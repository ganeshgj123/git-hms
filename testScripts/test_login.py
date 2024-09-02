from Utilities.ui_helpers import UiHelpers
from pytest import mark
from Utilities.excel_data import read_data,read_headers
from datetime import datetime

date_str = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")





headers = read_headers("login","test_user_login")
data = read_data("login","test_user_login")

@mark.parametrize(headers,data)
def test_user_login(pages,driver,username,password):
    print("executing test script")
    pages.homepage.admin_login()
    assert driver.title == "Admin-Login",f"{driver.save_screenshot(f"screenshots/{date_str}.png")}"
    pages.admin_loginpage.verify_valid_user_login(username,password)
    # assert "Manage Doctors" in driver.page_source,f"{driver.save_screenshot("screenshots/sample2.png")}"
    assert pages.admin_loginpage.is_valid_user_logged_in() == True,f"{driver.save_screenshot(f"screenshots/{date_str}.png")}"



headers = read_headers("login","test_invalid_user_login")
data = read_data("login","test_invalid_user_login")


@mark.parametrize(headers,data)
def test_invalid_user_login(pages,driver,username,password):
    print("executing test script")
    pages.homepage.admin_login()
    assert driver.title == "Admin-Login", f"{driver.save_screenshot(f"screenshots/{date_str}.png")}"
    pages.admin_loginpage.verify_valid_user_login(username, password)
    # assert "Manage Doctors" not in driver.page_source,f"{driver.save_screenshot("screenshots/sample2.png")}"
    assert pages.admin_loginpage.invalid_user_login() == True, f"{driver.save_screenshot(f"screenshots/{date_str}.png")}"





