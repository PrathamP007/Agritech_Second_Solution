from Pages.basePage import BasePage
from Locators.firstPage import Locators

class ResultPage(BasePage):
    def get_output_text(self):
        return self.get_text(Locators.OUTPUT_TEXT)
