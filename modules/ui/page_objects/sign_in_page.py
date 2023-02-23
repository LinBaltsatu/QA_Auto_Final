from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        login_field = self.driver.find_element(By.ID, "login_field")
        login_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)

    def click_sign_in(self):
        sign_in_button = self.driver.find_element(By.NAME, "commit")
        sign_in_button.click()

    def click_forgot_password(self):
        forgot_password_link = self.driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/a')
        forgot_password_link.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
    
    def check_error_message(self, expected_error):
        error_elem = self.driver.find_element(By.CLASS_NAME, "js-flash-alert")
        return error_elem.text == expected_error
    