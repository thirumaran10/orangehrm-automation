import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():  # browser -> session (expensive)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        yield browser
        browser.close()

@pytest.fixture
def context(browser):  # context -> function (isolation)
    context = browser.new_context(no_viewport=True)
    yield context
    context.close()

@pytest.fixture
def page(context):  # page -> function (disposable)
    page = context.new_page()
    yield page
    page.close()
