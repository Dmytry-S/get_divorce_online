from .common_wd_methods import CommonWebDriver
from .locators import Details3Locators


class Details3Page(CommonWebDriver):
    def any_minor_children(self):
        self.find_and_click_button(*Details3Locators.MINOR_CHILDREN)

    def is_wife_pregnant(self):
        self.find_and_click_button(*Details3Locators.IS_WIFE_PREGNANT)

    def find_and_click_button_save(self):
        self.find_and_click_button(*Details3Locators.BUTTON_SAVE)

