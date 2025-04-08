import pytest
import time

from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utilities.page_factory import PageFactory
from base.driver_class import Driver
import utilities.custom_logger as CL

# Initialize Logger
log = CL.custom_logger()


@pytest.fixture(scope="class")
def setup_class(request):
    log.info("Starting Automation tests")

    # Clear Allure reports before the test run
    CL.clear_allure_reports()

    # Initialize the driver
    driver = Driver().get_driver_method()
    request.cls.driver = driver
    request.cls.landing_page = LandingPage(request.cls.driver)
    request.cls.registration_page = RegistrationPage(request.cls.driver)
    request.cls.login_page = LoginPage(request.cls.driver)

    yield driver

    # Close the app
    time.sleep(1)
    driver.quit()
    log.info("Killing the application - Tests are done")


@pytest.fixture(scope="function")
def setup_function(request):
    log.info("Starting Automation tests")

    # Initialize the driver
    driver = Driver().get_driver_method()
    request.cls.driver = driver

    yield driver
    # Close the app
    time.sleep(1)
    driver.quit()
    log.info("Tests are done")
