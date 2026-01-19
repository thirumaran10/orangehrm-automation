
class ShopPage:
    def __init__(self,page):
        self.page = page

    def open_shop_tab(self):
        self.page.get_by_role("link", name = "Shop").click()

    def add_product_to_cart(self,product_name: str):
        #self.open_shop_tab()
        
        self.page.locator("app-card").filter(
            has=self.page.get_by_text(product_name)).get_by_role("button",name = "Add").click()
        
    def checkout_items(self):
        self.page.locator('//*[@class="nav-link btn btn-primary"]').click()



