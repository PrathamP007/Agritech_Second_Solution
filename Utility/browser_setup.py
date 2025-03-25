from selenium import webdriver
from utility.config import Config

class BrowserSetup:
    def __init__(self):
        self.driver = webdriver.Chrome(Config.DRIVER_PATH)
        self.driver.get(Config.BASE_URL)
        self.driver.maximize_window()

    def get_driver(self):
        return self.driver
