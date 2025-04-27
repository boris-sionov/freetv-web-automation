import os
import time

from base.base_page import BasePage
from utilities.config import ConfigReader
from base.files_path import screenshot_directory


class GeneralActions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.time_format = time.strftime(ConfigReader.read_config("date", "files_time_format"))

    def clean_screenshots_folder(self):
        # log = CL.custom_logger()

        if os.path.exists(screenshot_directory):
            try:
                for file_name in os.listdir(screenshot_directory):
                    file_path = os.path.join(screenshot_directory, file_name)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                self.log.info("Cleaned old screenshots from the folder.")
            except Exception as e:
                self.log.error(f"Error while cleaning screenshots folder: {str(e)}")
        else:
            self.log.error(f"Screenshot folder does not exist: {screenshot_directory}")

    def screenshot(self, screenshot_name):

        # Create the screenshot name with timestamp
        file_name = f"{screenshot_name}_{self.time_format}.png"
        screenshot_path = os.path.join(screenshot_directory, file_name)

        try:
            self.page.screenshot(path=screenshot_path, full_page=True)
            self.log.info("Screenshot saved to Path: " + screenshot_path)
            return file_name  # Return the file name
        except Exception as e:
            self.log.error(f"Unable to save screenshot to the Path: {screenshot_path}. Error: {str(e)}")

    def switch_to_frame(self, index):
        """
        Wait until the iframe at the given index is available and switch to it.
        :param index: Index of the iframe
        """
        try:
            self.log.info(f"Getting iframe at index {index}")
            frames = self.page.frames
            if index < len(frames):
                frame = frames[index]
                self.log.info(f"Frame at index {index} retrieved successfully.")
                return frame
            else:
                raise IndexError(f"No frame found at index {index}. Total frames: {len(frames)}")
        except Exception as e:
            self.log.error(f"Failed to get frame({index}). Error: {str(e)}")
            assert False, f"Failed to get frame({index}). Error: {str(e)}"
