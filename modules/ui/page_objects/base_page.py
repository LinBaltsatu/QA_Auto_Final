from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r"c:\Automation\Auto"
    DRIVER_NAME = "chromedriver.exe"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )

    def close(self):
        self.driver.close()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
