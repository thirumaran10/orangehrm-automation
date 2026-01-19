from pages.login_page import LoginPage

def test_login(page):
    
    login = LoginPage(page)
    login.open()
    # created a method open in login_page.py for navigating to the url
    login.login("rahulshettyacademy","Learning@830$3mK2")
    
    # for reusing the code we create a method in login_page.py and call that method here
    