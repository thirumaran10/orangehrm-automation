# '''import pytest
# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://demo.automationtesting.in/Alerts.html")
#     page.wait_for_load_state("networkidle") '''

# import pytest
# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     context = browser.new_context(no_viewport=True)
#     page.goto("https://rahulshettyacademy.com/loginpagePractise/", wait_until="networkidle")
#     page.fill('//input[@name="username"]','rahulshettyacademy')
#     page.fill('//input[@name="password"]','learning')
#     page.click('//input[@type="submit"]')
#     page.wait_for_timeout(15000)
#     #home page
#     page.click("//a[text()='Home']")
#     page.fill('(//input[@name="name"])[1]','Maran')
#     page.fill('//input[@name="email"]','sample@gmail.com')
#     page.fill('//input[@placeholder="Password"]','Password123')
#     page.check('//input[@id="exampleCheck1"]')
#     page.select_option('//select[@class="form-control"]', 'Male')
#     page.check('//input[@value="option2"]')
#     page.fill('(//input[@class="form-control"])[2]', '1999-05-01')

#     page.click('//input[@value="Submit"]')
#     msg = page.locator(".alert-success").text_content().strip()
#     print(msg)

#     assert "Success" in msg
#     page.wait_for_timeout(20000)