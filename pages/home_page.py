from playwright.sync_api import expect

#class name shold be upper case
class HomePage:
    def __init__(self, page):
        self.page = page

    def open_home_tab(self):
        self.page.get_by_role("link", name = "Home",  exact=True).click()

    def fill_home_page(self, name, email, password, gender, date_of_birth):
        self.open_home_tab()
        self.page.fill('(//input[@name="name"])[1]', name)
        self.page.fill('//input[@name="email"]', email)
        self.page.fill('//input[@placeholder="Password"]', password)
        self.page.check('//input[@id="exampleCheck1"]')
        self.page.select_option('//select[@class="form-control"]', gender)
        self.page.check('//input[@value="option2"]')
        self.page.fill('(//input[@class="form-control"])[2]', date_of_birth)
        self.page.get_by_role("button", name="Submit").click()

    def get_success_message(self):
        alert = self.page.locator(".alert-success")
        expect(alert).to_be_visible()
        return alert.text_content()