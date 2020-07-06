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
    MINOR_CHILDREN = (By.ID, "id_minor_children_0")
    IS_WIFE_PREGNANT = (By.ID, "id_wife_pregnant_primarily_1")
    BUTTON_SAVE = (By.CSS_SELECTOR, "button.tx-btn")


class Details4Locators:
    LIVE_TOGETHER = (By.ID, "id_live_together_now_0")
    COMMON_PROPERTY = (By.ID, "id_property_any_0")
    COMMON_DEBT = (By.ID, "id_debts_any_1")
    BUTTON_SAVE = (By.CSS_SELECTOR, "button.tx-btn")


class Details5Locators:
    PHONE_1 = (By.ID, "id_phone1")
    PHONE_1_VALUE = "123"
    PHONE_2 = (By.ID, "id_phone2")
    PHONE_2_VALUE = "678"
    PHONE_3 = (By.ID, "id_phone3")
    PHONE_3_VALUE = "5566"
    PASSWORD = (By.XPATH, "//input[@name='password']")
    PASSWORD_VALUE = "12345"
    BUTTON_SAVE = (By.CSS_SELECTOR, "form.form > .ml-0")
    CC_NUMBER = (By.ID, "id_ccnum")
    CC_NUMBER_VALUE = "4111111111111111"
    CC_EXP_MONTH = (By.ID, "id_ccexp_m")
    CC_EXP_MONTH_VALUE = "12"
    CC_EXP_YEAR = (By.ID, "id_ccexp_y")
    CC_EXP_YEAR_VALUE = "2023"
    ADDRESS = (By.ID, "id_addr1")
    ADDRESS_VALUE = "Street, 123"
    CITY = (By.ID, "id_city")
    CITY_VALUE = "Jersy"
    ZIP = (By.ID, "id_zip")
    ZIP_CODE = "43456"
    BUTTON_CONFIRM = (By.CSS_SELECTOR, "button.tx-btn")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".payment--non-field-errors")




