from robot.libraries.BuiltIn import BuiltIn

class BasePage:

    APP_URL = "https://jupiter.cloud.planittesting.com/"
    BROWSER = "Chrome"

    def __init__(self):
        self.driver = BuiltIn().get_library_instance('SeleniumLibrary')

    def open_browser_to_jupiter_toys_home_page(self):
        self.driver.open_browser(self.APP_URL, self.BROWSER)
        self.driver.maximize_browser_window()
        self.driver.set_selenium_implicit_wait(5)
        title = self.driver.get_title()
        print("Title of the page is: " + title)
        self.driver.title_should_be("Jupiter Toys")
