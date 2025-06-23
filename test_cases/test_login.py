import pytest
from pages.login_page import LoginPage

def test_valid_login(setup):
    login_page = LoginPage(setup)
    login_page.login("Admin", "admin123")
    assert login_page.is_login_successful(), "Login failed!"
