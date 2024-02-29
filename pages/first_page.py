from pages.base_page import BasePage
import time
from locators.first_page_locators import FirstPageLocators, PluginShopLocators, PluginInStaticLocators

locators = FirstPageLocators()

class FirstPage(BasePage):
    def go_to_menu(self):
        self.focus_window(locators.WINDOW)
        self.app.click(locators.MENU)
        time.sleep(5)

locators = PluginShopLocators()

class PluginshopPage(FirstPage):
    
    def go_to_pluginshop(self):
        self.quick_click(locators.PLUGINSHOP)
        self.quick_click(locators.DOWNLOAD_PLUGIN)
    
    def exitting_from_menu(self):
        self.quick_click(locators.EXIT)

locators = PluginInStaticLocators()

class PlaginInStaticPage(PluginshopPage):

    def download_monitoring_plugin(self):
        self.quick_click(locators.PLUGIN_MONITORING)
        self.ultra_long_click(locators.INSTALL_ALL)
        self.send_keys('{Esc}')
        
    def check_mer(self):
        self.quick_click(locators.STATIC)
        self.quick_click(locators.MER)
        self.quick_click(locators.EXPRORT_MER)

locators = PluginInStaticLocators()

class AutoHidePage(PlaginInStaticPage):

    def auto_hide(self):
        self.focus_window(locators.WINDOW)
        self.app.click(locators.STATIC)
        self.quick_click(locators.STATIC)
        self.quick_click(locators.STATIC)
        self.quick_click(locators.MER)
        self.quick_click(locators.EXPRORT_MER)
