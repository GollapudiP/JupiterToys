from robot.libraries.BuiltIn import BuiltIn

class HomePage:

    HOME = "id=nav-home"
    SHOP = "id=nav-shop"
    CONTACT = "id=nav-contact"
    CART = "id=nav-cart"

    def __init__(self):
         self.driver = BuiltIn().get_library_instance('SeleniumLibrary')

    def navigate_to_home(self):
        self.driver.click_element(self.HOME)
    
    def navigate_to_shop(self):
        self.driver.click_element(self.SHOP)

    def navigate_to_contact(self):
        self.driver.click_element(self.CONTACT)
        self.driver.wait_until_page_contains("We welcome your feedback", timeout=5)
    
    def navigate_to_cart(self):
        self.driver.click_element(self.CART)