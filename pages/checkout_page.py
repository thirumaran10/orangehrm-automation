class CheckoutPage:

    def __init__(self,page):
        self.page = page

    def increase_quantity(self,product_name: str,quantity: int):

        row = self.page.locator("tr").filter(has = self.page.get_by_text(product_name))
        row.locator("input[type = 'number']").fill(str(quantity))

    def get_total_amount(self) -> str:
        return self.page.locator("//h3/strong").inner_text()
    
    def final_checkout(self):
        self.page.get_by_role("button", name = "Checkout").click()

    

