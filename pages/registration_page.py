import time

import allure
from selenium.webdriver.common.by import By

import utilities.custom_logger as CL
from base.base_page import BasePage
from base.general_actions import GeneralActions
from base.ui_actions import UIActions
from base.ui_verifications import UIVerifications

# Initialize Logger
log = CL.custom_logger()


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.general_actions = GeneralActions(driver)
        self.ui_actions = UIActions(driver)
        self.ui_verifications = UIVerifications(driver)

    # Buttons
    __lets_start_btn = (By.CSS_SELECTOR, '.__1_btn__lmkJ0 > .Button_button_main__pamo6')
    __lets_continue_btn = (By.CSS_SELECTOR, '.Button_button_main__pamo6.__2_btn__86rzJ')
    __lets_continue_2_btn = (By.CSS_SELECTOR, '.w-full.mt-auto > .Button_button_main__pamo6')
    __freetv_2_btn = (By.CSS_SELECTOR, '.__2_plans__wQ74W > div:nth-child(2)')
    __lets_continue_3_btn = (By.CSS_SELECTOR, '.__2_products_btn__xotob > .Button_button_main__pamo6')
    __lets_continue_4_btn = (By.CSS_SELECTOR, '.w-full.mt-auto > .Button_button_main__pamo6')
    __privacy_agree = (By.CSS_SELECTOR, '.__2_privacy__ObHCR > div:nth-child(1)')
    __credit_card_btn = (By.CSS_SELECTOR, '.__2_payment_item__B7wMU > .__2_payment_item_wrapper__wUtRV')
    __add_credit_card_submit_btn = (By.ID, 'cg-submit-btn')
    __finish_progress_btn = (By.CSS_SELECTOR, '.__2_wrapper__gkKch > .Button_button_main__pamo6')

    # Form
    __enter_phone_number = (By.CSS_SELECTOR, '.FloatingInput_wrapper__eyHuD.border-gray-border')
    __first_name = (By.NAME, 'firstName')
    __last_name = (By.NAME, 'lastName')
    __card_number = (By.ID, 'card-number')
    __year = (By.ID, 'expYear')
    __month = (By.ID, 'expMonth')
    __cvv = (By.ID, 'cvv')
    __id_number = (By.ID, 'personal-id')

    # Text

    def press_on_lets_start(self):
        with allure.step("Step 1 - Press on בואו נתחיל button"):
            self.ui_actions.press(self.__lets_start_btn)

    def fill_in_phone_number(self, phone_number):
        with allure.step(f"Step 1 - Press on phone number field"):
            self.ui_actions.press(self.__enter_phone_number)
        with allure.step(f"Step 2 - Enter {phone_number} in phone number field"):
            self.ui_actions.fill_in_text_with_action_chain(phone_number)
        with allure.step("Step 3 - Press on בואו נמשיך button"):
            self.ui_actions.press(self.__lets_continue_btn)

    def fill_in_otp_code(self):
        with allure.step(f"Step 1 - Get OTP code from email"):
            otp_code = self.ui_actions.retrieve_otp_code()
        with allure.step(f"Step 2 - Enter {otp_code} in otp field"):
            self.ui_actions.fill_in_text_with_action_chain(otp_code)
        with allure.step("Step 3 - Press on בואו נמשיך button"):
            self.ui_actions.press(self.__lets_continue_2_btn)
        time.sleep(5)

    def click_on_freetv_2(self):
        with allure.step("Step 1 - Choose FreeTV 2 program"):
            self.ui_actions.press(self.__freetv_2_btn)
        with allure.step("Step 2 - Press on בואו נמשיך button"):
            self.ui_actions.press(self.__lets_continue_3_btn)
        with allure.step("Step 3 - Press on בואו נמשיך button"):
            self.ui_actions.press(self.__lets_continue_4_btn)

    def fill_user_info(self, first_name, last_name):
        with allure.step(f"Step 1 - Fill {first_name} in first name field"):
            self.ui_actions.fill_in_text(self.__first_name, first_name)
        with allure.step(f"Step 2 - Fill {last_name} in last name field"):
            self.ui_actions.fill_in_text(self.__last_name, last_name)

    def fill_credit_card_info(self, credit_card, year_exp, month_exp, cvv, id_number):
        with allure.step(f"Step 1 - Press on add credit card button"):
            self.ui_actions.press(self.__credit_card_btn)
            time.sleep(5)

        with allure.step(f"Step 2 - Switch to iframe"):
            self.general_actions.switch_to_frame(0)
        with allure.step(f"Step 3 - Fill in credit card number"):
            self.ui_actions.fill_in_text(self.__card_number, credit_card, )
        with allure.step(f"Step 4 - Fill in expiration year"):
            self.ui_actions.select_from_options(self.__year, year_exp)
        with allure.step(f"Step 5 - Fill in expiration month"):
            self.ui_actions.select_from_options(self.__month, month_exp)
        with allure.step(f"Step 6 - Fill in CVV"):
            self.ui_actions.fill_in_text(self.__cvv, cvv)
        with allure.step(f"Step 7 - Fill ID"):
            self.ui_actions.fill_in_text(self.__id_number, id_number)
        with allure.step(f"Step 8 - Press on add credit card button"):
            self.ui_actions.press(self.__add_credit_card_submit_btn)

    def click_on_privacy_agree(self):
        with allure.step(f"Step 1 - Switch to main frame"):
            self.driver.switch_to.default_content()
            time.sleep(5)
        with allure.step(f"Step 2 - Press on agree to privacy"):
            self.ui_actions.press(self.__privacy_agree)

    def click_on_finish(self):
        with allure.step(f"Step 1 - Press on finish button"):
            self.ui_actions.press(self.__finish_progress_btn)
