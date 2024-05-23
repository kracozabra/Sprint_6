import allure
from pages.main_page import MainPage


class TestRedirect:

    @allure.title('Проверка перехода по ссылке с лого Самоката')
    def test_redirect_from_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_order_url()
        main_page.click_scooter_logo()
        current_url = main_page.get_current_url()

        assert current_url == main_page.MAIN_URL, 'Не открылась главная страница https://qa-scooter.praktikum-services.ru'

    @allure.title('Проверка перехода по ссылке с лого Яндекса')
    def test_redirect_from_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_order_url()
        main_page.click_yandex_logo()
        main_page.switch_new_tab()
        main_page.wait_for_title('Дзен')
        current_url = main_page.get_current_url()

        assert 'https://dzen.ru/' in current_url, 'Не открылась страница https://dzen.ru/'
