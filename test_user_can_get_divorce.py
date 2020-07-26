import pytest
from pages.details_1 import Details1Page
from pages.details_2 import Details2Page
from pages.details_3 import Details3Page
from pages.details_4 import Details4Page
from pages.details_5 import Details5Page
from pages.login_page import LoginPage


@pytest.mark.run_test
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

    def test_user_can_fill_page_details5(self, browser):
        link = "https://onlineminnesotadivorce.com/minnesota/details/5/"
        page = Details5Page(browser, link)
        page.open_url()
        page.enter_phone_number()
        page.enter_password()
        page.find_and_click_button_save()
        page.enter_credit_card_number()
        page.enter_expiration_month()
        page.enter_expiration_year()
        page.enter_address()
        page.enter_city_name()
        page.enter_zip_code()
        page.find_and_click_button_confirm()
        page.is_error_message_present()

