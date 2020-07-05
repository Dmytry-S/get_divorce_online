from selenium.webdriver.common.by import By


class LoginPageLocators:
    FIRST_NAME = (By.ID, "id_first_name")
    FIRST_NAME_VALUE = "Tom"
    LAST_NAME = (By.ID, "id_last_name")
    LAST_NAME_VALUE = "jerry"
    EMAIL = (By.XPATH, "//input[@name='email']")
    BUTTON_CHECK = (By.CSS_SELECTOR, "button.tx-btn")


class Details1Locators:
    YOU_ARE = (By.ID, "id_you_are_0")
    SELECT_DUTY_MILITARY = (By.CSS_SELECTOR, ".filter-option")
    YES = (By.XPATH, "//span[text()='Yes']")
    BUTTON_SAVE = (By.CSS_SELECTOR, "button.tx-btn")


class Details2Locators:
    DATE_OF_MARRIAGE = (By.ID, "id_date_of_marriage")
    MARRIAGE_DATE = "11111990"
    IS_A_SAME_SEX = (By.ID, "id_were_you_in_a_same-sex_marriage_1")
    PERSON_FILLING_FILE = (By.ID, "id_who_will_file_0")
    BUTTON_SAVE = (By.CSS_SELECTOR, "button.tx-btn")


class Details3Locators:
    pass


class Details4Locators:
    pass


class Details5Locators:
    pass


