import time

import allure
from selenium.webdriver.common.by import By

import utilities.custom_logger as CL
from base.base_page import BasePage
from base.ui_actions import UIActions
from base.ui_verifications import UIVerifications

# Initialize Logger
log = CL.custom_logger()


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.ui_actions = UIActions(driver)
        self.ui_verifications = UIVerifications(driver)

    # Buttons
    __register_btn = (By.CSS_SELECTOR, '.Hero_btn__LNbtR > .Button_button_main__pamo6')
    __go_btn = (By.XPATH, ".//button[text()='קדימה']")
    __profile_button = (By.CSS_SELECTOR, '.navbar__subscriber-account')
    __my_account = (By.XPATH, "//span[@class='link__title' and text()='החשבון שלי']")
    __delete_account_btn = (By.CSS_SELECTOR, '.button--cancel')

    __cancel_account_btn = (By.XPATH, "//button[text()='לביטול המינוי']")

    # Form
    __phone_number_field = (By.ID, 'msisdn')
    __otp_code_field = (By.ID, 'input_0')

    def press_on_login(self):
        self.ui_actions.press(self.__go_btn)

    def fill_in_phone_number(self, phone_nuber):
        self.ui_actions.fill_in_text(self.__phone_number_field, phone_nuber)

    def press_on_kadima(self):
        self.ui_actions.press(self.__go_btn)

    def fill_otp_code(self):
        otp_code = self.ui_actions.retrieve_otp_code()
        self.ui_actions.fill_in_text(self.__otp_code_field, otp_code)

    def press_on_profile(self):
        self.ui_actions.press_with_action_chain(self.__profile_button)
        self.ui_actions.press(self.__my_account)
        self.ui_actions.press(self.__delete_account_btn)
        time.sleep(5)
        self.driver.switch_to.frame(0)
        self.ui_actions.press(self.__cancel_account_btn)
        time.sleep(5)





