from robot.libraries.BuiltIn import BuiltIn

class ShopPage:

    def __init__(self):
         self.driver = BuiltIn().get_library_instance('SeleniumLibrary')

    def add_item_to_cart(self, item):
        item_locator = f"xpath://h4[text()='{item}']/following-sibling::p/a"
        self.driver.click_element(item_locator)