import allure
from base.base_page import BasePage
from base.ui_actions import UIActions


class LandingPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.ui_actions = UIActions(page)

    # Buttons
    __register_btn = '.Hero_btn__LNbtR > .Button_button_main__pamo6'
    __register_btn1 = 'role=link[name="קבלו חודש ניסיון חינם"]'
    __login_btn = "// *[@title = 'כניסה']"

    def press_on_signup(self):
        with allure.step("Step 1 - Press on registration button"):
            self.ui_actions.press(self.__register_btn1)

    # def press_on_login(self):
    #     with allure.step("Step 1 - Press on login button"):
    #         self.base_page.press(self.__login_btn)
