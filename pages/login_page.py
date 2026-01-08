class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username="rahulshettyacademy", password="learning"):
        self.page.fill('//input[@name="username"]', username)
        self.page.fill('//input[@name="password"]', password)  # this method used for reusing the code for login
        self.page.click('//input[@type="submit"]')

