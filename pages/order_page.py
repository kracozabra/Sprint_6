import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):

    _ORDER_FORM = [By.XPATH, "//div[contains(@class, 'Order_Form')]"]
    _NAME_FIELD = [By.XPATH, "//input[contains(@placeholder, 'Имя')]"]
    _SURNAME_FIELD = [By.XPATH, "//input[contains(@placeholder, 'Фамилия')]"]
    _ADDRESS_FIELD = [By.XPATH, "//input[contains(@placeholder, 'Адрес')]"]
    _METRO_FIELD = [By.XPATH, "//input[contains(@placeholder, 'Станция метро')]"]
    _METRO_LIST_ITEM_XPATH = "//input[contains(@placeholder, 'Станция метро')]/../..//li[{0}]"
    _PHONE_FIELD = [By.XPATH, "//input[contains(@placeholder, 'Телефон')]"]
    _ORDER_NEXT_BUTTON = [By.XPATH, "//button[text()='Далее']"]
    _ORDER_FORM_RENT_HEADER = [By.XPATH, "//div[contains(@class,'Order_Header') and (text()='Про аренду')]"]
    _DATE_FIELD = [By.XPATH, "//input[contains(@placeholder, 'Когда привезти')]"]
    _PERIOD_FIELD = [By.XPATH, "//div[contains(text(), 'Срок аренды')]/.."]
    _PERIOD_ITEM_XPATH = "//div[contains(text(), 'Срок аренды')]/../..//div[@role='option'][{0}]"
    _BLACK_COLOR_FIELD = [By.XPATH, "//label[contains(text(), 'чёрный жемчуг')]"]
    _GREY_COLOR_FIELD = [By.XPATH, "//label[contains(text(), 'серая безысходность')]"]
    _COMMENT_FIELD = [By.XPATH, "//input[contains(@placeholder, 'Комментарий')]"]
    _ORDER_BUTTON = [By.XPATH, "//div[contains(@class, 'Order_Content')]//button[text()='Заказать']"]
    _ORDER_CONFIRMATION_MODAL_HEADER = [By.XPATH, "//div[contains(@class,'Order_ModalHeader') and text()='Хотите оформить заказ?']"]
    _ORDER_CONFIRMED_MODAL_HEADER = [By.XPATH, "//div[contains(@class,'Order_ModalHeader')]"]
    _CONFIRM_ORDER_BUTTON = [By.XPATH, "//button[contains(@class,'Button_Button') and (text()='Да')]"]

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ждем загрузки формы заказа')
    def wait_order_page_loaded(self):
        self.wait_for_element_visible(self._ORDER_FORM)

    @allure.step('Заполняем Имя')
    def set_name(self, name):
        self.enter_text(self._NAME_FIELD, name)

    @allure.step('Заполняем Фамилию')
    def set_surname(self, surname):
        self.enter_text(self._SURNAME_FIELD, surname)

    @allure.step('Заполняем Адрес')
    def set_address(self, address):
        self.enter_text(self._ADDRESS_FIELD, address)

    @allure.step('Выбираем станцию Метро')
    def select_metro(self, metro):
        self.click_element(self._METRO_FIELD)
        metro_list_item = [By.XPATH, self._METRO_LIST_ITEM_XPATH.format(metro)]
        self.click_element(metro_list_item)

    @allure.step('Заполняем Телефон')
    def set_phone(self, phone):
        self.enter_text(self._PHONE_FIELD, phone)

    @allure.step('Кликаем на кнопку "Далее"')
    def click_order_next_button(self):
        self.click_element(self._ORDER_NEXT_BUTTON)

    @allure.step('Ожидаем загрузку второй страницы заказа')
    def wait_second_page_order(self):
        self.wait_for_element_visible(self._ORDER_FORM_RENT_HEADER)

    @allure.step('Заполняем Дату')
    def set_date(self, date):
        self.enter_text(self._DATE_FIELD, date)

    @allure.step('Закрываем календарь, чтобы не мешал заполнять следующие поля')
    def close_calendar(self):
        self.click_element(self._ORDER_FORM_RENT_HEADER)

    @allure.step('Выбираем Период аренды')
    def set_period(self, period):
        self.click_element(self._PERIOD_FIELD)
        period_item = [By.XPATH, self._PERIOD_ITEM_XPATH.format(period)]
        self.click_element(period_item)

    @allure.step('Выбираем Цвет')
    def set_color(self, color):
        if color == 'black':
            self.click_element(self._BLACK_COLOR_FIELD)
        if color == 'grey':
            self.click_element(self._GREY_COLOR_FIELD)

    @allure.step('Заполняем Комментарий')
    def set_comment(self, comment):
        self.enter_text(self._COMMENT_FIELD, comment)

    @allure.step('Кликаем на кнопку "Заказать"')
    def click_order_button(self):
        self.click_element(self._ORDER_BUTTON)

    @allure.step('Кликаем на кнопку подтверждения заказа')
    def click_confirm_order_button(self):
        self.wait_for_element_visible(self._CONFIRM_ORDER_BUTTON)
        self.click_element(self._CONFIRM_ORDER_BUTTON)

    @allure.step('Получаем заголовок финального диалогового окна')
    def get_modal_header(self):
        self.wait_for_element_visible(self._ORDER_CONFIRMED_MODAL_HEADER)
        return self.find_element(self._ORDER_CONFIRMED_MODAL_HEADER).text

    @allure.step('Заполняем все поля формы и размещаем заказ ')
    def fill_order_form(self, name, surname, metro, address, phone, date, period, color, comment):
        self.set_name(name)
        self.set_surname(surname)
        self.select_metro(metro)
        self.set_address(address)
        self.set_phone(phone)
        self.click_order_next_button()
        self.wait_second_page_order()
        self.set_date(date)
        self.close_calendar()
        self.set_period(period)
        self.set_color(color)
        self.set_comment(comment)
        self.click_order_button()
        self.click_confirm_order_button()
