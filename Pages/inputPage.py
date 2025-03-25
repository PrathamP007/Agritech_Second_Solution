from Pages.basePage import BasePage
from Locators.firstPage import Locators

class InputPage(BasePage):
    def enter_text(self, text):
        self.send_keys(Locators.INPUT_FIELD, text)

    def click_submit(self):
        self.click(Locators.SUBMIT_BUTTON)
