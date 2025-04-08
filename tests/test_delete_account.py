import time

import allure
import pytest

from utilities.page_factory import PageFactory


@pytest.mark.usefixtures("setup_class")
class TestDelete(PageFactory):

    @allure.description("Test 01 - Open FreeTV website")
    def test_01_press_on_login(self):
        self.landing_page.press_on_login()

    @allure.description("Test 02 - Enter phone number")
    def test_02_enter_phone_number(self):
        self.login_page.fill_in_phone_number('0504963671')
        self.login_page.press_on_kadima()
        self.login_page.fill_otp_code()

    def test_03_open_menu(self):
        self.login_page.press_on_profile()
