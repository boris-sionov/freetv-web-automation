import email
import imaplib
import re
import time
from email.utils import parsedate_to_datetime

from base.base_page import BasePage
from utilities.config import ConfigReader


class UIActions(BasePage):

    def __init__(self, page, page_obj):
        super().__init__(page)
        self.page_obj = page_obj

    def press(self, locator):
        try:
            element = self.wait_for_element_enabled(locator)
            element.click()
            self.log.info(f"Clicked on '{locator}' element")
        except Exception as e:
            self.log.error(f"Error while clicking on element: {locator}. Exception: {e}")

    def fill_in_text(self, locator, text):
        try:
            element = self.wait_for_element_enabled(locator)
            element.fill(text)
            self.log.info(f"Filled '{text}' into '{locator}' element")
        except Exception as e:
            self.log.error(f"Error while filling text into element: {locator}. Exception: {e}")

    def get_text(self, locator):
        element = self.wait_for_element_enabled(locator)
        element_text = element.inner_text()
        self.log.info(f"Text from {locator} is: {element_text}")
        return element_text

    def select_from_drop_down(self, locator, text):
        element = self.wait_for_element_enabled(locator)
        element.select_option(value=text)
        self.log.info(f"Selected '{text}' from dropdown element '{locator}'")

    def frame_actions(self, action, frame, locator, text=None):
        try:
            in_frame_element = self.wait_for_element_in_frame(frame, locator)
            if action == "fill" and text is not None:
                in_frame_element.fill(text)
                self.log.info(f"Filled '{text}' into element '{locator}' in frame '{frame}'.")

            elif action == "select" and text is not None:
                in_frame_element.select_option(text)
                self.log.info(f"Selected '{text}' from element '{locator}' in frame '{frame}'.")

            elif action == "click":
                in_frame_element.click()
                self.log.info(f"Clicked on element '{locator}' in frame '{frame}'.")

            else:
                self.log.warning(f"Unsupported action '{action}' or missing 'text' value for locator '{locator}'.")

        except Exception as e:
            self.log.error(f"Action '{action}' on element '{locator}' in frame '{frame}' failed: {e}")
            raise

    def retrieve_otp_code(self, timeout=60, poll_interval=5):
        imap_server = "imap.gmx.com"
        email_address = ConfigReader.read_config("otp", "email")
        password = ConfigReader.read_config("otp", "password")

        start_time = time.time()
        self.log.info("Connecting to GMX IMAP server...")

        try:
            mail = imaplib.IMAP4_SSL(imap_server)
            mail.login(email_address, password)
            mail.select("inbox")
            self.log.info("Connected to GMX email account and inbox selected.")
        except Exception as e:
            self.log.error(f"Failed to connect/login: {e}")
            assert False, f"Failed to connect/login to GMX IMAP server: {e}"

        otp_code = None

        while time.time() - start_time < timeout:
            try:
                status, messages = mail.search(None, "(UNSEEN)")
                email_ids = messages[0].split()

                if not email_ids:
                    self.log.info("No new emails yet. Retrying...")
                    time.sleep(poll_interval)
                    continue

                latest_email_id = email_ids[-1]
                status, msg_data = mail.fetch(latest_email_id, "(RFC822)")

                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        email_datetime = parsedate_to_datetime(msg.get("Date"))

                        if email_datetime.timestamp() < start_time:
                            continue

                        body = ""
                        if msg.is_multipart():
                            for part in msg.walk():
                                if part.get_content_type() == "text/plain":
                                    body = part.get_payload(decode=True).decode()
                                    break
                        else:
                            body = msg.get_payload(decode=True).decode()

                        otp_match = re.search(r"קוד האימות שלך.*?(\d{4,8})", body)
                        if otp_match:
                            otp_code = otp_match.group(1)
                            self.log.info(f"OTP successfully retrieved: {otp_code}")

                            mail.store(latest_email_id, '+FLAGS', '\\Deleted')
                            mail.expunge()
                            self.log.info("OTP email deleted from inbox.")
                            break
            except Exception as e:
                self.log.error(f"Error while reading email: {e}")

            if otp_code:
                break
            else:
                time.sleep(poll_interval)

        mail.logout()

        if not otp_code:
            self.log.error("OTP email not received within timeout.")
            assert False, "OTP email not received within timeout."

        return otp_code

    def fill_in_otp(self, page_obj, otp_code):
        otp_code_str = str(otp_code)
        for i, digit in enumerate(otp_code_str, start=1):
            locator_attr_name = f"_{type(page_obj).__name__}__OTP_digit{i}"
            locator = getattr(page_obj, locator_attr_name)
            self.fill_in_text(locator, digit)
