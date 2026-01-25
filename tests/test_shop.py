from pages.login_page import LoginPage
from pages.shop_page import ShopPage


def test_add_products_to_cart(page):
    login= LoginPage(page)
    login.open()
    login.login("rahulshettyacademy","Learning@830$3mK2")
    
    shop = ShopPage(page)
    shop.open_shop_tab()

    products = ["Samsung Note 8","Nokia Edge","Blackberry"]

    for product in products:
        shop.add_product_to_cart(product)

    Checkout = shop.checkout_items()

    Checkout.increase_quantity("Nokia Edge",2)
    Checkout.increase_quantity("Blackberry",3)
    total = Checkout.get_total_amount()
    print(total)

    placing_order = Checkout.final_checkout()
    placing_order.place_order("Indi", "India")
    msg = placing_order.get_success_message()
    assert "Success" in msg




        

