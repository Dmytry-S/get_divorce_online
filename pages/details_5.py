from .common_wd_methods import CommonWebDriver
from .locators import Details5Locators


class Details5Page(CommonWebDriver):
    def enter_phone_number(self):
        self.find_and_send_keys(*Details5Locators.PHONE_1, Details5Locators.PHONE_1_VALUE)
        self.find_and_send_keys(*Details5Locators.PHONE_2, Details5Locators.PHONE_2_VALUE)
        self.find_and_send_keys(*Details5Locators.PHONE_3, Details5Locators.PHONE_3_VALUE)

    def enter_password(self):
        self.find_and_send_keys(*Details5Locators.PASSWORD, Details5Locators.PASSWORD_VALUE)

    def find_and_click_button_save(self):
        self.find_and_click_button(*Details5Locators.BUTTON_SAVE)

    def enter_credit_card_number(self):
        self.find_and_send_keys(*Details5Locators.CC_NUMBER, Details5Locators.CC_NUMBER_VALUE)

    def enter_expiration_month(self):
        self.find_element_in_list(*Details5Locators.CC_EXP_MONTH, Details5Locators.CC_EXP_MONTH_VALUE)

    def enter_expiration_year(self):
        self.find_element_in_list(*Details5Locators.CC_EXP_YEAR, Details5Locators.CC_EXP_YEAR_VALUE)

    def enter_address(self):
        self.find_and_send_keys(*Details5Locators.ADDRESS, Details5Locators.ADDRESS_VALUE)

    def enter_city_name(self):
        self.find_and_send_keys(*Details5Locators.CITY, Details5Locators.CITY_VALUE)

    def enter_zip_code(self):
        self.find_and_send_keys(*Details5Locators.ZIP, Details5Locators.ZIP_CODE)

    def find_and_click_button_confirm(self):
        self.find_and_click_button(*Details5Locators.BUTTON_CONFIRM)

    def is_error_message_present(self):
        self.is_element_present(*Details5Locators.ERROR_MESSAGE)

