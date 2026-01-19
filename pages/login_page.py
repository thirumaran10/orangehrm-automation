from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    def login(self, username, password):
        self.page.fill('//input[@name="username"]', username)
        self.page.fill('//input[@name="password"]', password)  # this method used for reusing the code for login
        self.page.click('//input[@type="submit"]')

    # basic validation
        expect(self.page).to_have_url("https://rahulshettyacademy.com/angularpractice/shop")
        


