import time

import allure
import pytest

from utilities.config import ConfigReader
from utilities.page_factory import PageFactory


@pytest.mark.usefixtures("setup_class")
class TestLogin(PageFactory):

    @allure.description("Test 01 - Open FreeTV website and start registration progress")
    def test_01_open_freetv_website(self):
        self.landing_page.press_on_signup()

    @allure.description("Test 02 - Start registration progress")
    def test_02_press_on_let_start(self):
        self.registration_page.press_on_lets_start()
        time.sleep(5)

    @allure.description("Test 03 - Enter phone number")
    def test_03_enter_phone_number(self):
        phone_number = ConfigReader.read_config("account", "phone_number")
        self.registration_page.fill_in_phone_number(phone_number)

    @allure.description("Test 04 - Fill in OTP code received from email`")
    def test_04_enter_otp_code(self):
        self.registration_page.fill_in_otp_code()

    @allure.description("Test 05 - Start Choose FreeTV 2 program")
    def test_05_click_on_freetv_2(self):
        self.registration_page.click_on_freetv_2()

    @allure.description("Test 06 - Fill in name and sure name of the account")
    def test_06_fill_in_names(self):
        first_name = ConfigReader.read_config('account', 'first_name')
        last_name = ConfigReader.read_config('account', 'last_name')
        self.registration_page.fill_user_info(first_name, last_name)

    @allure.description("Test 07 - Fill in credit card info")
    def test_07_enter_credit_card_info(self):
        # Add credit card info before running
        credit_card = ConfigReader.read_config("credit_card", "card_number")
        year_exp = ConfigReader.read_config("credit_card", "year_exp")
        month_exp = ConfigReader.read_config("credit_card", "month_exp")
        cvv = ConfigReader.read_config("credit_card", "cvv")
        id_number = ConfigReader.read_config("credit_card", "id_number")
        self.registration_page.fill_credit_card_info(credit_card, year_exp, month_exp, cvv, id_number)

    @allure.description("Test 08 - Finish Registration")
    def test_08_finish(self):
        self.registration_page.click_on_privacy_agree()
        # self.registration_page.click_on_finish()
