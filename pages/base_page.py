from RPA.Windows import Windows
import time

class BasePage:
    def __init__(self, app: Windows):
        self.app = app
        time.sleep(5)

    def focus_window(self, locator):
        self.app.control_window(locator)
        time.sleep(5)

    def send_keys(self, locator):
        self.app.send_keys(keys=locator)
        time.sleep(5)

    def quick_click(self, locator):
        self.app.click(locator)
        time.sleep(5)

    def medium_click(self, locator):
        self.app.click(locator)
        time.sleep(30)

    def long_click(self, locator):
        self.app.click(locator)
        time.sleep(60)

    def ultra_long_click(self, locator):
        self.app.click(locator)
        time.sleep(300)
