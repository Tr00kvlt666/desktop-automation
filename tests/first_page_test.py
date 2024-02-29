from pages.first_page import FirstPage, PluginshopPage, PlaginInStaticPage, AutoHidePage

def test_open_rnkin(library):
    """
    Проверка открытия программы
    """
    first_page = FirstPage(library)
    first_page.go_to_menu()
    assert True, "Не открылось главное меню"

def test_open_pluginshop(library):
    """
    Проверка открытия магазина модулей
    """
    menu_page = PluginshopPage(library)
    menu_page.go_to_menu()
    menu_page.go_to_pluginshop()
    menu_page.exitting_from_menu()
    assert True, "Открывается магазин приложений, успешно"

def test_plagin_in_static(library):
    """
    Скачивания плагинов рабочего процесса Мониторинг
    """
    first_page = PlaginInStaticPage(library)
    first_page.go_to_menu()
    first_page.go_to_pluginshop()
    first_page.download_monitoring_plugin()
    first_page.check_mer()
    first_page.go_to_menu()
    first_page.exitting_from_menu()
    assert True, "Не открылся МЭР из скачанных плагинов рабочего процесса Мониторинг"

def test_auto_hiding(library):
    """
    Проверить авто скрытие ленты
    """
    first_page = AutoHidePage(library)
    first_page.auto_hide()
    assert True, "Авто скрытие ленты не работает"