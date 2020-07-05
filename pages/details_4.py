from .common_wd_methods import CommonWebDriver
from .locators import Details4Locators


class Details4Page(CommonWebDriver):
    def live_in_same_house_with_spouse(self):
        self.find_and_click_button(*Details4Locators.LIVE_TOGETHER)

    def have_common_property_with_spouse(self):
        self.find_and_click_button(*Details4Locators.COMMON_PROPERTY)

    def have_common_debt_with_spouse(self):
        self.find_and_click_button(*Details4Locators.COMMON_DEBT)

    def find_and_click_button_save(self):
        self.find_and_click_button(*Details4Locators.BUTTON_SAVE)