# browser_init.py
import configparser
from playwright.sync_api import sync_playwright

from utilities.config import ConfigReader


def get_browser_from_config():
    # Read browser type from config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Read the browser type from the [web] section
    browser_type = ConfigReader.read_config('web', 'browser')  # Default to 'chromium' if not set
    return browser_type


def initialize_browser():
    browser_type = get_browser_from_config()

    with sync_playwright() as p:
        if browser_type == "chromium":
            browser = p.chromium.launch(headless=False)
        elif browser_type == "firefox":
            browser = p.firefox.launch(headless=False)
        elif browser_type == "webkit":
            browser = p.webkit.launch(headless=False)
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")

        return browser
