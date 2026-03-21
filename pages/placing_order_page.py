from playwright.sync_api import expect

class PlacingOrderPage:

    def __init__(self, page):
        self.page = page

    def place_order(self,country_prefix:str, country_fullname: str):
       
        country_input = self.page.locator("input[id='country']")
        country_input.type(country_prefix, delay=100)
        suggestion = self.page.locator(".suggestions ul li a") 
        suggestion.first.wait_for(state = "visible")
        
        suggestion.filter(has_text = country_fullname).click()     

        self.page.wait_for_timeout(300)
        self.page.locator("//*[text()='India']").click()

        self.page.locator("label[for='checkbox2']").click()
        self.page.get_by_role("button", name = "Purchase").click()
    
    def get_success_message(self):
        alert = self.page.locator(".alert-success")
        expect(alert).to_be_visible()
        return alert.text_content()   
    