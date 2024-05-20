import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class MainPage(BasePage):

    _FAQ_SECTION_LOCATOR = [By.XPATH, "//div[contains(@class, 'Home_FAQ')]"]
    _QUESTION_LOCATOR = [By.XPATH, "//div[contains(@class, 'Home_FAQ')]//div[1]/div[contains(@class, 'accordion__heading')]/div"]
    _ANSWER_LOCATOR = [By.XPATH, "//div[contains(@class, 'Home_FAQ')]//div[1]/div[contains(@class, 'accordion__panel')]/p"]
    _TOP_ORDER_BUTTON = [By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']"]
    _BOTTOM_ORDER_BUTTON = [By.XPATH, "//div[contains(@class,'FinishButton')]//button"]

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидаем загрузку блока FAQ')
    def wait_for_load_faq_section(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self._FAQ_SECTION_LOCATOR))

    @allure.step('Скроллим страницу до блока FAQ')
    def scroll_to_faq_section(self):
        element = self.driver.find_element(*self._FAQ_SECTION_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Кликаем на плашку вопроса')
    def click_question_tab(self, tab_number):
        # Пришлось переопределить некоторые локаторы внутри функций, т. к. номер таба в XPATH зависит от параметра теста
        # Если есть какой-то более правильный способ это сделать, то хотелось бы о нем узнать)
        _QUESTION_LOCATOR = [By.XPATH, f"//div[contains(@class, 'Home_FAQ')]//div[{tab_number}]/div[contains(@class, 'accordion__heading')]/div"]
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(_QUESTION_LOCATOR))
        self.driver.find_element(*_QUESTION_LOCATOR).click()

    @allure.step('Получаем текст вопроса')
    def get_question_text(self, tab_number):
        _QUESTION_LOCATOR = [By.XPATH, f"//div[contains(@class, 'Home_FAQ')]//div[{tab_number}]/div[contains(@class, 'accordion__heading')]/div"]
        return self.driver.find_element(*_QUESTION_LOCATOR).text

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, tab_number):
        _ANSWER_LOCATOR = [By.XPATH, f"//div[contains(@class, 'Home_FAQ')]//div[{tab_number}]/div[contains(@class, 'accordion__panel')]/p"]
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(_ANSWER_LOCATOR))
        return self.driver.find_element(*_ANSWER_LOCATOR).text

    @allure.step('Ждем появления кнопки "Заказать" внизу страницы')
    def wait_bottom_order_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self._BOTTOM_ORDER_BUTTON))

    @allure.step('Кликаем на кнопку "Заказать" внизу страницы')
    def click_bottom_order_button(self):
        self.driver.find_element(*self._BOTTOM_ORDER_BUTTON).click()

    @allure.step('Кликаем на кнопку "Заказать" в хэдере')
    def click_top_order_button(self):
        self.driver.find_element(*self._TOP_ORDER_BUTTON).click()
