#class name shold be upper case
class HomePage:
    def __init__(self, page):
        self.page = page

    def fill_home_page(self):
        self.page.click("//a[text()='Home']")
        self.page.fill('(//input[@name="name"])[1]','Maran')
        self.page.fill('//input[@name="email"]','sample@gmail.com')
        self.page.fill('//input[@placeholder="Password"]','Password123')
        self.page.check('//input[@id="exampleCheck1"]')
        self.page.select_option('//select[@class="form-control"]', 'Male')
        self.page.check('//input[@value="option2"]')
        self.page.fill('(//input[@class="form-control"])[2]', '1999-05-01')
        self.page.click('//input[@value="Submit"]')

    def get_success_message(self):
        return self.page.locator(".alert-success").text_content().strip()