
from playwright.sync_api import expect

#class name shold be upper case
class HomePage:
    def __init__(self, page):
        self.page = page

    def fill_home_page(self, name='Maran', email='sample@gmail.com', password='Password123', gender='Male', date_of_birth='1999-05-01'):
        self.page.click("//a[text()='Home']")
        self.page.fill('(//input[@name="name"])[1]', name)
        self.page.fill('//input[@name="email"]', email)
        self.page.fill('//input[@placeholder="Password"]', password)
        self.page.check('//input[@id="exampleCheck1"]')
        self.page.select_option('//select[@class="form-control"]', gender)
        self.page.check('//input[@value="option2"]')
        self.page.fill('(//input[@class="form-control"])[2]', date_of_birth)
        self.page.click('//input[@value="Submit"]')

    def get_success_message(self):
        alert = self.page.locator(".alert-success")
        expect(alert).to_be_visible(timeout=5000)
        return alert.text_content().strip()
        