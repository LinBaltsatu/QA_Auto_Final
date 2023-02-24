from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


# Перевірка назви сторінки при спробі залогінитися
# з неправильним юзернеймом та паролем
@pytest.mark.ui
def test_check_incorrest_username_page_object(sign_in_page):
    sign_in_page.enter_username("wrong_email@gmail.com")
    sign_in_page.enter_password("wrong_password")
    sign_in_page.click_sign_in()
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


# Перевірка повідомлення про помилку при спробі залогінітися
# без введення юзернейму та паролю
@pytest.mark.ui
def test_login_with_empty_fields(sign_in_page):
    sign_in_page.click_sign_in()
    assert sign_in_page.check_error_message("Incorrect username or password.")


# Перевірка назви сторінки при кліку на лінку Forgot password?
@pytest.mark.ui
def test_check_opening_forgot_password_page(sign_in_page):
    sign_in_page.click_forgot_password()
    assert sign_in_page.check_title("Forgot your password? · GitHub")
