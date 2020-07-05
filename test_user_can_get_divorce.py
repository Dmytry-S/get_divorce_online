import pytest
from pages.login_page import LoginPage
from pages.details_1 import Details1Page
from pages.details_2 import Details2Page
from pages.details_3 import Details3Page
from pages.details_4 import Details4Page
import time


@pytest.mark.mock
class TestUserCanGetOnlineDivorce:
    def test_user_can_sign_up(self, browser):
        link = "https://onlineminnesotadivorce.com/"
        page = LoginPage(browser, link)
        page.open_url()
        page.find_and_send_first_name()
        page.find_and_send_last_name()
        page.find_and_send_email()
        page.find_and_click_button_check()

    def test_user_can_fill_page_details1(self, browser):
        link = "https://onlineminnesotadivorce.com/minnesota/details/1/"
        page = Details1Page(browser, link)
        page.open_url()
        page.find_and_click_you_are()
        page.select_active_duty_military()
        page.find_and_click_button_save()

    def test_user_can_fill_page_details2(self, browser):
        link = "https://onlineminnesotadivorce.com/minnesota/details/2/"
        page = Details2Page(browser, link)
        page.open_url()
        page.fill_marriage_date()
        page.is_same_sex_marriage()
        page.person_filling_file()
        page.find_and_click_button_save()

    def test_user_can_fill_page_details3(self, browser):
        link = "https://onlineminnesotadivorce.com/minnesota/details/3/"
        page = Details3Page(browser, link)
        page.open_url()
        page.any_minor_children()
        page.is_wife_pregnant()
        page.find_and_click_button_save()

    def test_user_can_fill_page_details4(self, browser):
        link = "https://onlineminnesotadivorce.com/minnesota/details/4/"
        page = Details4Page(browser, link)
        page.open_url()
        page.live_in_same_house_with_spouse()
        page.have_common_property_with_spouse()
        page.have_common_debt_with_spouse()
        page.find_and_click_button_save()
        time.sleep(10)