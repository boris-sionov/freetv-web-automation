
import allure
from selenium.webdriver.common.by import By

import utilities.custom_logger as CL
from base.base_page import BasePage
from base.ui_actions import UIActions
from base.ui_verifications import UIVerifications

# Initialize Logger
log = CL.custom_logger()


class LandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.ui_actions = UIActions(driver)
        self.ui_verifications = UIVerifications(driver)

    # Buttons
    __register_btn = (By.CSS_SELECTOR, '.Hero_btn__LNbtR > .Button_button_main__pamo6')
    __login_btn = (By.XPATH, "// *[@title = 'כניסה']")

    # Form

    # Text

    def press_on_signup(self):
        with allure.step("Step 1 - Press on registration button"):
            self.ui_actions.press(self.__register_btn)

    def press_on_login(self):
        with allure.step("Step 1 - Press on login button"):
            self.ui_actions.press(self.__login_btn)
