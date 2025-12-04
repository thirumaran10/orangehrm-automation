import pytest
from playwright.sync_api import sync_playwright

def test_open_browser(page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/", wait_until="networkidle")
    page.fill('//input[@name="username"]','rahulshettyacademy')
    page.fill('//input[@name="password"]','learning')
    page.click('//input[@type="submit"]')
    page.wait_for_timeout(15000)

