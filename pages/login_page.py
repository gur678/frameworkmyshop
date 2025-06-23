from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    DASHBOARD = (By.XPATH, "//h6[text()='Dashboard']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        self.wait.until(EC.presence_of_element_located(self.USERNAME)).send_keys(username)
        self.wait.until(EC.presence_of_element_located(self.PASSWORD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN)).click()

    def is_login_successful(self):
        return self.wait.until(EC.visibility_of_element_located(self.DASHBOARD)).is_displayed()
