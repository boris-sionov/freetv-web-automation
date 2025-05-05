import pytest

import utilities.custom_logger as CL
from utilities.config import ConfigReader
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
    url_test_link = ConfigReader.read_config("web", "url")
    request.cls.page.goto(url_test_link)

    # Loop through all pages in PageFactory and create instances dynamically
    for page_name, page_class in PageFactory.__annotations__.items():
        # Dynamically initialize each page and add it to request.cls
        page_instance = page_class(page)
        setattr(request.cls, page_name, page_instance)

    yield
    # Close the app
    request.cls.page.close()
    browser.close()
