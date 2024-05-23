import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    _FAQ_SECTION = [By.XPATH, "//div[contains(@class, 'Home_FAQ')]"]
    _QUESTION_XPATH = "//div[contains(@class, 'Home_FAQ')]//div[{0}]/div[contains(@class, 'accordion__heading')]/div"
    _ANSWER_XPATH = "//div[contains(@class, 'Home_FAQ')]//div[{0}]/div[contains(@class, 'accordion__panel')]/p"
    _TOP_ORDER_BUTTON = [By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']"]
    _BOTTOM_ORDER_BUTTON = [By.XPATH, "//div[contains(@class,'FinishButton')]//button"]

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидаем загрузку блока FAQ')
    def wait_for_load_faq_section(self):
        self.wait_for_element_visible(self._FAQ_SECTION)

    @allure.step('Скроллим страницу до блока FAQ')
    def scroll_to_faq_section(self):
        self.scroll_to_element(self._FAQ_SECTION)

    @allure.step('Кликаем на плашку вопроса')
    def click_question_tab(self, tab_number):
        # Пришлось переопределить некоторые локаторы внутри функций, т. к. номер таба в XPATH зависит от параметра теста
        # Если есть какой-то более правильный способ это сделать, то хотелось бы о нем узнать)
        question_locator = [By.XPATH, self._QUESTION_XPATH.format(tab_number)]
        self.wait_for_element_visible(question_locator)
        self.click_element(question_locator)

    @allure.step('Получаем текст вопроса')
    def get_question_text(self, tab_number):
        question_locator = [By.XPATH, self._QUESTION_XPATH.format(tab_number)]
        question_text = self.find_element(question_locator).text
        return question_text

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, tab_number):
        answer_locator = [By.XPATH, self._ANSWER_XPATH.format(tab_number)]
        self.wait_for_element_visible(answer_locator)
        answer_text = self.find_element(answer_locator).text
        return answer_text

    @allure.step('Ждем появления кнопки "Заказать" внизу страницы')
    def wait_bottom_order_button(self):
        self.wait_for_element_visible(self._BOTTOM_ORDER_BUTTON)

    @allure.step('Кликаем на кнопку "Заказать" внизу страницы')
    def click_bottom_order_button(self):
        self.click_element(self._BOTTOM_ORDER_BUTTON)

    @allure.step('Кликаем на кнопку "Заказать" в хэдере')
    def click_top_order_button(self):
        self.click_element(self._TOP_ORDER_BUTTON)
