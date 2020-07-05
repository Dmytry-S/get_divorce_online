from .common_wd_methods import CommonWebDriver
from .locators import Details2Locators


class Details2Page(CommonWebDriver):
    def fill_marriage_date(self):
        self.find_and_send_keys(*Details2Locators.DATE_OF_MARRIAGE, Details2Locators.MARRIAGE_DATE)

    def is_same_sex_marriage(self):
        self.find_and_click_button(*Details2Locators.IS_A_SAME_SEX)

    def person_filling_file(self):
        self.find_and_click_button(*Details2Locators.PERSON_FILLING_FILE)

    def find_and_click_button_save(self):
        self.find_and_click_button(*Details2Locators.BUTTON_SAVE)

