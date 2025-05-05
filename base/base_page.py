import utilities.custom_logger as CL
from playwright.sync_api import expect
from twilio.rest import Client
import re
from datetime import datetime, timezone
import time

from utilities.config import ConfigReader


class BasePage:

    def __init__(self, page):
        self.page = page
        self.log = CL.custom_logger()

    def wait_for_element_enabled(self, locator, timeout=10000):
        self.log.info(f"Waiting for element '{locator}' to be enabled.")
        element = self.page.locator(locator)
        element.wait_for(state="attached", timeout=timeout)
        expect(element).to_be_enabled(timeout=timeout)
        return element

    def wait_for_element_in_frame(self, frame, locator, timeout=5000):
        self.log.info(f"Waiting for element '{locator}' inside frame '{frame}' for up to {timeout}ms  .")

        try:
            in_frame_element = self.page.frame_locator(frame).locator(locator)
            expect(in_frame_element).to_be_visible(timeout=timeout)
            self.log.info(f"Element '{locator}' is now visible inside frame '{frame}'.")
            return in_frame_element

        except Exception as e:
            self.log.error(f"Element '{locator}' not found in frame '{frame}' within {timeout}ms. Exception: {e}")
            raise Exception(f"Element '{locator}' not found in frame '{frame}' within {timeout}ms.") from e

    def get_latest_otp(self, timeout=60):
        account_sid = ConfigReader.read_config("twillo", "sid")
        auth_token = ConfigReader.read_config("twillo", "token")

        client = Client(account_sid, auth_token)

        end_time = time.time() + timeout
        utc_time = datetime.now(timezone.utc)
        local_time = utc_time.astimezone()

        self.log.info(f"Waiting for SMS after {local_time.strftime(ConfigReader.read_config('date', 'twillo_time_format'))}")

        while time.time() < end_time:
            messages = client.messages.list(limit=5)

            for msg in messages:
                # Check if the message is newer than when we started
                if msg.date_sent and msg.date_sent > local_time:
                    match = re.search(r"\b\d{4,6}\b", msg.body)
                    message_time = msg.date_sent.astimezone()
                    if match:
                        otp = match.group()
                        self.log.info(f"OTP found: {otp} at time: {message_time.strftime(ConfigReader.read_config('date', 'twillo_time_format'))}")
                        return otp

            time.sleep(3)  # Wait before polling again

        self.log.warning("Timed out waiting for OTP.")
        return None

