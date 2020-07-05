import time
from .common_wd_methods import CommonWebDriver
from .locators import LoginPageLocators


class LoginPage(CommonWebDriver):
    def find_and_send_first_name(self):
        self.find_and_send_keys(*LoginPageLocators.FIRST_NAME, LoginPageLocators.FIRST_NAME_VALUE)

    def find_and_send_last_name(self):
        self.find_and_send_keys(*LoginPageLocators.LAST_NAME, LoginPageLocators.LAST_NAME_VALUE)

    def find_and_send_email(self):
        email = str(time.time()) + "@fakemail.org"
        self.find_and_send_keys(*LoginPageLocators.EMAIL, email)

    def find_and_click_button_check(self):
        self.find_and_click_button(*LoginPageLocators.BUTTON_CHECK)




