from Utilities.excel_reader import attach_locator
from Utilities.ui_helpers import UiHelpers

from time import sleep
from selenium.common import NoSuchElementException

@attach_locator("admin_page")
class AdminLoginPage(UiHelpers):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


#optional
    # email = ("xpath",'//input[@name="username"]')
    # password = ("xpath",'//input[@name="password"]')
    # login_button = ("xpath",'//button[@name="submit"]')
    # user = ("xpath","//h2[text()='Manage Doctors']")


    def verify_valid_user_login(self,username,password):
        self.enter_text(self.email,value=username)
        self.enter_text(self.password,value=password)
        self.click_element(self.login_button)

    def is_valid_user_logged_in(self):
        return self.check_element_visible(self.user)

    def invalid_user_login(self):
        return self.check_element_visible(self.invalid_user)































