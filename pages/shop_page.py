from pages.checkout_page import CheckoutPage

class ShopPage:
    def __init__(self,page):
        self.page = page

    def open_shop_tab(self):
        self.page.get_by_role("link", name = "Shop").click()

    def add_product_to_cart(self,product_name: str):

        # find all the product cards
        cards = self.page.locator("app-card")

        # filter the cards to find the one with the given product name
        selected_cards = cards.filter(has=self.page.get_by_text(product_name))
        
        # find the add button inside the selected card 
        add_button = selected_cards.get_by_role("button",name = "Add")
        add_button.click() # click the add button
        
    def checkout_items(self):
        self.page.locator('//*[@class="nav-link btn btn-primary"]').click()
        return CheckoutPage(self.page)


