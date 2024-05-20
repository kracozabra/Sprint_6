import allure
import time
from selenium import webdriver
from pages.base_page import BasePage


class TestRedirect:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка перехода по ссылке с лого Самоката')
    def test_redirect_from_scooter_logo(self):
        base_page = BasePage(self.driver)
        base_page.open_order_url()
        base_page.click_scooter_logo()

        assert self.driver.current_url == base_page.MAIN_URL, 'Не открылась главная страница https://qa-scooter.praktikum-services.ru'

    @allure.title('Проверка перехода по ссылке с лого Яндекса')
    def test_redirect_from_yandex_logo(self):
        base_page = BasePage(self.driver)
        base_page.open_order_url()
        base_page.click_yandex_logo()
        time.sleep(3)
        current_url = base_page.get_new_tab_url()

        assert 'https://dzen.ru/' in current_url, 'Не открылась страница https://dzen.ru/'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
