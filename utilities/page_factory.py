from appium.webdriver.webdriver import WebDriver

from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


class PageFactory:
    driver: WebDriver
    landing_page = LandingPage
    registration_page = RegistrationPage
    login_page = LoginPage
