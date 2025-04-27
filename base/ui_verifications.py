import time

import allure

from base.base_page import BasePage
from base.general_actions import GeneralActions
from base.files_path import screenshot_directory


class UIVerifications(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.general_actions = GeneralActions(page)

    def verify_text_in_element(self, locator, expected_text):
        element = self.wait_for_element_enabled(locator)
        actual_text = element.text

        if expected_text == actual_text:
            with allure.step(f"Text verification passed: '{actual_text}' matches expected '{expected_text}'."):
                self.log.info(f"Text verification passed: '{actual_text}' matches expected '{expected_text}'.")
        else:
            screenshot_path = screenshot_directory + self.general_actions.screenshot("Text_Verification_Fail")
            with allure.step(f"Text verification failed: Expected '{expected_text}', but got '{actual_text}'."):
                allure.attach.file(screenshot_path, name="Text Verification Failure Screenshot", attachment_type=allure.attachment_type.PNG)
                self.log.error(f"Text verification failed: Expected '{expected_text}', but got '{actual_text}'.")
            assert expected_text == actual_text, f"Expected text: '{expected_text}', but got: '{actual_text}'"
