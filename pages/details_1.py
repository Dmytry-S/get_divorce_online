from .common_wd_methods import CommonWebDriver
from .locators import Details1Locators


class Details1Page(CommonWebDriver):
    def find_and_click_you_are(self):
        self.find_and_click_button(*Details1Locators.YOU_ARE)

    def select_active_duty_military(self):
        self.find_and_click_button(*Details1Locators.SELECT_DUTY_MILITARY)
        self.find_and_click_button(*Details1Locators.YES)

    def find_and_click_button_save(self):
        self.find_and_click_button(*Details1Locators.BUTTON_SAVE)
