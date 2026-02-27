from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_form_submit(page):

    login = LoginPage(page)
    login.open()  # navigate to login page
    login.login("rahulshettyacademy","Learning@830$3mK2")  # perform login

    home = HomePage(page) # create POM object
    home.fill_home_page(name="Maran", 
                        email="sample@gmail.com", 
                        password="Password123", 
                        gender="Male", 
                        date_of_birth="1999-05-01") # fill form and submit
    
    msg = home.get_success_message() # capture success message
    assert "Success" in msg


