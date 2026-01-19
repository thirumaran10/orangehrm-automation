import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():  # browser -> session (expensive)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()



