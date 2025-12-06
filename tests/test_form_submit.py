from pages.home_page import HomePage
from playwright.sync_api import expect

def test_form_submit(page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/", wait_until="networkidle")
    home = HomePage(page) # create POM object
    home.fill_home_page() # fill form and submit
    msg = home.get_success_message() # capture success message
    print(msg)
    assert "Success" in msg
    page.wait_for_timeout(15000)


