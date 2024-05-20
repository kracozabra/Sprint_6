import allure
import pytest
from selenium import webdriver
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import order_form_data


class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка создания заказа по кнопке из хедера')
    def test_create_order_from_top_button(self):
        main_page = MainPage(self.driver)
        main_page.open_main_url()
        main_page.click_accept_cookie_button()
        main_page.click_top_order_button()

        order_page = OrderPage(self.driver)
        order_page.fill_order_form(*order_form_data[0])
        actual_modal_header = order_page.get_modal_header()

        assert 'Заказ оформлен' in actual_modal_header, 'Не появилось окно с текстом "Заказ оформлен"'

    @allure.title('Проверка создания заказа по кнопке внизу страницы')
    @pytest.mark.parametrize('name,surname,metro,address,phone,date,period,color,comment', order_form_data)
    def test_create_order_from_bottom_button(self, name, surname, metro, address, phone, date, period, color, comment):
        main_page = MainPage(self.driver)
        main_page.open_main_url()
        main_page.click_accept_cookie_button()
        main_page.wait_bottom_order_button()
        main_page.click_bottom_order_button()

        order_page = OrderPage(self.driver)
        order_page.fill_order_form(name, surname, metro, address, phone, date, period, color, comment)
        actual_modal_header = order_page.get_modal_header()

        assert 'Заказ оформлен' in actual_modal_header, 'Не появилось окно с текстом "Заказ оформлен"'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()