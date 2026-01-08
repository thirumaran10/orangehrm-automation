from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_form_submit(page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    login = LoginPage(page)
    login.login()  # perform login

    home = HomePage(page) # create POM object
    home.fill_home_page() # fill form and submit
    
    msg = home.get_success_message() # capture success message
    print(msg)
    assert "Success" in msg


