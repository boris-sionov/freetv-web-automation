import utilities.custom_logger as CL
from playwright.sync_api import expect


class BasePage:

    def __init__(self, page):
        self.__page = page
        self.log = CL.custom_logger()

    def wait_for_element_enabled(self, locator, timeout=5000):
        self.log.info(f"Waiting for element '{locator}' to be enabled.")
        element = self.__page.locator(locator)
        element.wait_for(state="attached", timeout=timeout)
        expect(element).to_be_enabled(timeout=timeout)
        return element

    def wait_for_element_in_frame(self, frame, locator, timeout=5000):
        self.log.info(f"Waiting for element '{locator}' inside frame '{frame}' for up to {timeout}ms.")

        try:
            # Locate the element inside the frame
            in_frame_element = self.__page.frame_locator(frame).locator(locator)

            # Use Playwright's `expect` to wait for visibility
            expect(in_frame_element).to_be_visible(timeout=timeout)

            self.log.info(f"Element '{locator}' is now visible inside frame '{frame}'.")
            return in_frame_element

        except Exception as e:
            self.log.error(f"Element '{locator}' not found in frame '{frame}' within {timeout}ms. Exception: {e}")
            raise Exception(f"Element '{locator}' not found in frame '{frame}' within {timeout}ms.") from e
