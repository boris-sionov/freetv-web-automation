import pytest
import time

import utilities.custom_logger as CL
from pages.landing_page import LandingPage
from pages.registration_page import RegistrationPage
from utilities.page_factory import PageFactory

# Initialize Logger
log = CL.custom_logger()


@pytest.fixture(scope="class", autouse=True)
def setup_class(request, browser):
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},  # simulate full screen
        screen={"width": 1920, "height": 1080}
    )
    page = context.new_page()
    request.cls.page = page
    request.cls.page.goto("https://freetv.tv/")

    # Loop through all pages in PageFactory and create instances dynamically
    for page_name, page_class in PageFactory.__annotations__.items():
        # Dynamically initialize each page and add it to request.cls
        page_instance = page_class(page)
        setattr(request.cls, page_name, page_instance)


    yield
    # Close the app
    request.cls.page.close()
    browser.close()
