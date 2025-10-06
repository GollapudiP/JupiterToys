from robot.libraries.BuiltIn import BuiltIn

class ContactPage:

    SUBMIT = "xpath://a[text()='Submit']"
    FORENAME = "id:forename"
    EMAIL = "id:email"
    MESSAGE = "id:message"

    def __init__(self):
         self.driver = BuiltIn().get_library_instance('SeleniumLibrary')

    def submit_feedback(self):
        self.driver.click_element(self.SUBMIT)
        self.driver.wait_until_page_contains("We welcome your feedback", timeout=5)

    def verify_error_messages(self):
        self.driver.page_should_contain("Forename is required")
        self.driver.page_should_contain("Email is required")
        self.driver.page_should_contain("Message is required")

    def populate_mandatory_fields(self, forename, email, message):
        self.driver.input_text(self.FORENAME, forename)
        self.driver.input_text(self.EMAIL, email)
        self.driver.input_text(self.MESSAGE, message)

    def verify_no_error_messages_are_shown(self):
        self.driver.page_should_not_contain("Forename is required")
        self.driver.page_should_not_contain("Email is required")
        self.driver.page_should_not_contain("Message is required")

    def verify_feedback_successful_submission_message(self, forename):
        self.driver.wait_until_page_contains(f"Thanks {forename}, we appreciate your feedback.", timeout=15)