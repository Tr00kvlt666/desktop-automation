class MainMenuLocators:
    WINDOW = "regex:window"
    MENU = "Главное меню"

class FirstPageLocators(MainMenuLocators):
    PATH_FOR_INSTALL = "D:\\Установочный файл\\test\\launcher_for_install.exe" 
    PATH = "D:\programm\launcher.exe"
    LOGIN = 'INKhazipov'    
    PASSWORD = '1234568'   
    PATH_EXIT = "taskkill /T /f /im launcher.exe"

class PluginShopLocators(FirstPageLocators):
    PLUGINSHOP = "Магазин модулей"
    DOWNLOAD_PLUGIN = "Скачать"
    EXIT = "Выход"

class PluginInStaticLocators(PluginShopLocators):
    PLUGIN_MONITORING = "Мониторинг месторождений"
    INSTALL_ALL = "Всё"
    STATIC = "Static"
    MER = "МЭР"
    EXPRORT_MER = "Экспорт"
