from Utilities.ui_helpers import UiHelpers
from pytest import mark
from Utilities.excel_data import read_data,read_headers
from datetime import datetime


@mark.parametrize("username,password,doctor_specialisation",[("admin","Test@12345","Pediatric Surgeon")])
def test_tc1_added_doctor_specialisation(pages,driver,username,password,doctor_specialisation):
    pages.homepage.admin_login()
    pages.admin_loginpage.verify_valid_user_login(username,password)
    pages.admin_loginpage.is_valid_user_logged_in()
    pages.admin_dashbordpage.click_doc_specialisation_page()
    assert pages.admin_dashbordpage.verify_specialisation_page_visible() == True
    pages.admin_dashbordpage.create_doctor_specialisation(doctor_specialisation)
    assert pages.admin_dashbordpage.verify_created_doctor_specialisation() == True

@mark.parametrize("username,password",[("admin","Test@12345")])
def test_tc2_doctor_update_specialisation(pages,driver,username,password):
    pages.homepage.admin_login()
    pages.admin_loginpage.verify_valid_user_login(username, password)
    pages.admin_loginpage.is_valid_user_logged_in()
    pages.admin_dashbordpage.click_doctors()
    pages.admin_dashbordpage.click_doc_specialisation_page()
    assert True == pages.admin_dashbordpage.verify_specialisation_page_visible()








