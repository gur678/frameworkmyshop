from pages.login_page import LoginPage

def test_invalid_login(setup):
    driver = setup
    login = LoginPage(driver)
    login.click_sign_in()
    login.login("invalid@email.com", "wrongpassword")
    assert "Authentication failed." in login.get_error()
