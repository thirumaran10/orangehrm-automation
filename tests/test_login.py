from pages.login_page import LoginPage

def test_login(page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    login = LoginPage(page)
    login.login()
    
# for reusing the code we create a method in login_page.py and call that method here
