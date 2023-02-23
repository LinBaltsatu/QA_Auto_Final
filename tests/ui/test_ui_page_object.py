from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrest_username_page_object():
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    sign_in_page.enter_username("wrong_email@gmail.com")
    sign_in_page.enter_password("wrong_password")
    sign_in_page.click_sign_in()
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")
    sign_in_page.close()


@pytest.mark.ui
def test_login_with_empty_fields():
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    sign_in_page.click_sign_in()
    assert sign_in_page.check_error_message("Incorrect username or password.")
    sign_in_page.close()      


@pytest.mark.ui
def test_check_opening_forgot_password_page():
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    sign_in_page.click_forgot_password()
    assert sign_in_page.check_title("Forgot your password? · GitHub")
    sign_in_page.close()  

