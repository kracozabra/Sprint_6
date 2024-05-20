import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class OrderPage(BasePage):

    _ORDER_FORM = [By.XPATH, "//div[contains(@class, 'Order_Form')]"]
    _NAME_FIELD = [By.XPATH, "//input[contains(@placeholder, 'Имя')]"]
    _SURNAME_FIELD = [By.XPATH, "//input[contains(@placeholder, 'Фамилия')]"]
    _ADDRESS_FIELD = [By.XPATH, "//input[contains(@placeholder, 'Адрес')]"]
    _METRO_FIELD = [By.XPATH, "//input[contains(@placeholder, 'Станция метро')]"]
    _METRO_LIST_ITEM = [By.XPATH, "//input[contains(@placeholder, 'Станция метро')]/../..//li"]
    _PHONE_FIELD = [By.XPATH, "//input[contains(@placeholder, 'Телефон')]"]
    _ORDER_NEXT_BUTTON = [By.XPATH, "//button[text()='Далее']"]
    _ORDER_FORM_RENT_HEADER = [By.XPATH, "//div[contains(@class,'Order_Header') and (text()='Про аренду')]"]
    _DATE_FIELD = [By.XPATH, "//input[contains(@placeholder, 'Когда привезти')]"]
    _PERIOD_FIELD = [By.XPATH, "//div[contains(text(), 'Срок аренды')]/.."]
    _PERIOD_ITEM = [By.XPATH, "//div[contains(text(), 'Срок аренды')]/../..//div[@role='option']"]
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
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self._ORDER_FORM))

    @allure.step('Заполняем Имя')
    def set_name(self, name):
        self.driver.find_element(*self._NAME_FIELD).send_keys(name)

    @allure.step('Заполняем Фамилию')
    def set_surname(self, surname):
        self.driver.find_element(*self._SURNAME_FIELD).send_keys(surname)

    @allure.step('Заполняем Адрес')
    def set_address(self, address):
        self.driver.find_element(*self._ADDRESS_FIELD).send_keys(address)

    @allure.step('Выбираем станцию Метро')
    def select_metro(self, metro):
        self.driver.find_element(*self._METRO_FIELD).click()
        _METRO_LIST_ITEM = [By.XPATH, f"//input[contains(@placeholder, 'Станция метро')]/../..//li[{metro}]"]
        self.driver.find_element(*_METRO_LIST_ITEM).click()

    @allure.step('Заполняем Телефон')
    def set_phone(self, phone):
        self.driver.find_element(*self._PHONE_FIELD).send_keys(phone)

    @allure.step('Кликаем на кнопку "Далее"')
    def click_order_next_button(self):
        self.driver.find_element(*self._ORDER_NEXT_BUTTON).click()

    @allure.step('Ожидаем загрузку второй страницы заказа')
    def wait_second_page_order(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self._ORDER_FORM_RENT_HEADER))

    @allure.step('Заполняем Дату')
    def set_date(self, date):
        self.driver.find_element(*self._DATE_FIELD).send_keys(date)

    @allure.step('Закрываем календарь, чтобы не мешал заполнять следующие поля')
    def close_calendar(self):
        self.driver.find_element(*self._ORDER_FORM_RENT_HEADER).click()

    @allure.step('Выбираем Период аренды')
    def set_period(self, period):
        self.driver.find_element(*self._PERIOD_FIELD).click()
        _PERIOD_ITEM = [By.XPATH, f"//div[contains(text(), 'Срок аренды')]/../..//div[@role='option'][{period}]"]
        self.driver.find_element(*_PERIOD_ITEM).click()

    @allure.step('Выбираем Цвет')
    def set_color(self, color):
        if color == 'black':
            self.driver.find_element(*self._BLACK_COLOR_FIELD).click()
        if color == 'grey':
            self.driver.find_element(*self._GREY_COLOR_FIELD).click()

    @allure.step('Заполняем Комментарий')
    def set_comment(self, comment):
        self.driver.find_element(*self._COMMENT_FIELD).send_keys(comment)

    @allure.step('Кликаем на кнопку "Заказать"')
    def click_order_button(self):
        self.driver.find_element(*self._ORDER_BUTTON).click()

    @allure.step('Кликаем на кнопку подтверждения заказа')
    def click_confirm_order_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self._ORDER_CONFIRMATION_MODAL_HEADER))
        self.driver.find_element(*self._CONFIRM_ORDER_BUTTON).click()

    @allure.step('Получаем заголовок финального диалогового окна')
    def get_modal_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self._ORDER_CONFIRMED_MODAL_HEADER))
        return self.driver.find_element(*self._ORDER_CONFIRMED_MODAL_HEADER).text

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
