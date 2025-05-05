
import allure

from base.base_page import BasePage
from base.general_actions import GeneralActions
from base.ui_actions import UIActions
from base.ui_verifications import UIVerifications


class RegistrationPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.general_actions = GeneralActions(page)
        self.ui_actions = UIActions(page)
        self.ui_verifications = UIVerifications(page)
        # self.page = page

    # -------------------- Buttons --------------------
    __lets_start_btn = 'role=button[name="בואו נתחיל"]'
    __lets_continue_btn = 'role=button[name="בואו נמשיך"]'
    __lets_continue_btn_last = '.w-full.mt-auto > .Button_button_main__pamo6'
    __freetv_2_btn = 'role=button[name="FREE 2 ₪ 44.90 לחודש"]'

    __privacy_agree = 'role=checkbox[name="קראתי ואישרתי"]'
    __credit_card_btn = 'role=button[name="מספר כרטיס אשראי"]'

    __add_credit_card_submit_btn = '#cg-submit-btn'
    __finish_progress_btn = '.__2_wrapper__gkKch > .Button_button_main__pamo6'

    # -------------------- Form Fields --------------------
    __enter_phone_number = 'role=textbox[name="* טלפון"]'
    __OTP_digit1 = 'role=textbox[name="יש להזין קוד אימות שנשלח אליך בSMS - ספרה ראשונה"]'
    __OTP_digit2 = 'role=textbox[name="ספרה שניה"]'
    __OTP_digit3 = 'role=textbox[name="ספרה שלישית"]'
    __OTP_digit4 = 'role=textbox[name="ספרה רביעית"]'
    __first_name = '[name="firstName"]'
    __last_name = '[name="lastName"]'

    # -------------------- Frame and Credit Card Fields --------------------
    __frame = "#ua_main_aria iframe"
    __card_number = '#card-number'
    __exp_year = '#expYear'
    __month = '#expMonth'
    __cvv = '#cvv'
    __id_number = '#personal-id'

    def press_on_lets_start(self):
        with allure.step("Step 1 - Press on בואו נתחיל button"):
            self.ui_actions.press(self.__lets_start_btn)

    def fill_in_phone_number(self, phone_number):
        with allure.step(f"Step 1 - Enter {phone_number} in phone number field"):
            self.ui_actions.fill_in_text(self.__enter_phone_number, phone_number)
            # time.sleep(2)
        with allure.step("Step 3 - Press on בואו נמשיך button"):
            self.ui_actions.press(self.__lets_continue_btn)

    def fill_in_otp_code(self):
        with allure.step("Fill in OTP code"):
            otp_code = self.ui_actions.retrieve_otp_from_twillo()
            self.ui_actions.fill_in_otp(self, otp_code)
            self.ui_actions.press(self.__lets_continue_btn)

    def click_on_freetv_2(self):
        with allure.step("Choose FreeTV 2 program"):
            self.ui_actions.press(self.__freetv_2_btn)
            self.ui_actions.press(self.__lets_continue_btn)
            self.ui_actions.press(self.__lets_continue_btn_last)

    def fill_user_info(self, first_name, last_name):
        with allure.step("Fill user information"):
            self.ui_actions.fill_in_text(self.__first_name, first_name)
            self.ui_actions.fill_in_text(self.__last_name, last_name)

    def fill_credit_card_info(self, credit_card, year, month, cvv, id_number):
        with allure.step("Fill credit card information"):
            self.ui_actions.press(self.__credit_card_btn)
            self.ui_actions.frame_actions("fill", self.__frame, self.__card_number, credit_card)
            self.ui_actions.frame_actions("select", self.__frame, self.__exp_year, year)
            self.ui_actions.frame_actions("select", self.__frame, self.__month, month)
            self.ui_actions.frame_actions("fill", self.__frame, self.__cvv, cvv)
            self.ui_actions.frame_actions("fill", self.__frame, self.__id_number, id_number)
            self.ui_actions.frame_actions("click", self.__frame, self.__add_credit_card_submit_btn)

    def click_on_privacy_agree(self):
        with allure.step(f"Agree to privacy policy"):
            self.ui_actions.press(self.__privacy_agree)

    def click_on_finish(self):
        with allure.step(f"Step 1 - Press on finish button"):
            self.ui_actions.press(self.__finish_progress_btn)
