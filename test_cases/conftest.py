import os
import pytest
from selenium import webdriver
from Utilities.logger import get_logger
logger = get_logger(__name__)

@pytest.fixture
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    logger.info("Launched browser and navigated to OrangeHRM")

    yield driver

    if request.node.rep_call.failed:
        screenshot_path = f"screenshots/{request.node.name}.png"
        driver.save_screenshot(screenshot_path)
        logger.error(f"Test failed. Screenshot saved to {screenshot_path}")
    driver.quit()
    logger.info("Closed browser")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to access test result for screenshot"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("Reports/failure_log.txt") else "w"
        with open("Reports/failure_log.txt", mode) as f:
            if hasattr(item, 'rep_call'):
                screenshot_file = f"{item.name}.png"
                f.write(f"{item.name} failed. Screenshot: Screenshots/{screenshot_file}\n")
