from robot.libraries.BuiltIn import BuiltIn

class CartPage:

    TOTAL_PRICE = "xpath=//tfoot//strong"

    def __init__(self):
         self.driver = BuiltIn().get_library_instance('SeleniumLibrary')

    def update_quantity_of_item(self, item, quantity):
        item_quantity_locator = f"xpath=//td[contains(text(), '{item}')]/following-sibling::td[2]/input"
        self.driver.input_text(item_quantity_locator, quantity)

    def verify_price_of_the_item(self, item, expected_price):
        item_price_locator = f"xpath=//td[contains(text(), '{item}')]/following-sibling::td[1]"
        actual_price = self.driver.get_text(item_price_locator)
        if actual_price == expected_price:
            print(f"Price of the product '{item}' is as expected: {expected_price}")
        else:
            raise Exception(f"Price of the product '{item}' is not as expected. Expected: {expected_price}, Actual: {actual_price}")

    def verify_subtotal_of_the_item(self, item, expected_subtotal):
        item_subtotal_locator = f"xpath=//td[contains(text(), '{item}')]/following-sibling::td[3]"
        actual_subtotal = self.driver.get_text(item_subtotal_locator)   
        if actual_subtotal == expected_subtotal:
            print(f"Subtotal of the product '{item}' is as expected: {expected_subtotal}")
        else:
            raise Exception(f"Subtotal of the product '{item}' is not as expected. Expected: {expected_subtotal}, Actual: {actual_subtotal}")   

    def verify_the_total_price(self, expected_total):
        total_price_locator = self.TOTAL_PRICE
        actual_total = self.driver.get_text(total_price_locator)
        if actual_total == expected_total:
            print(f"Total price is as expected: {expected_total}")
        else:
            raise Exception(f"Total price is not as expected. Expected: {expected_total}, Actual: {actual_total}")
