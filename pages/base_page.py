import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    _ACCEPT_COOKIE_BUTTON = [By.XPATH, "//button[contains(@class,'App_CookieButton')]"]
    _SCOOTER_LOGO = [By.XPATH, "//a[contains(@class, 'LogoScooter')]"]
    _YANDEX_LOGO = [By.XPATH, "//a[contains(@class, 'LogoYandex')]"]

    MAIN_URL = "https://qa-scooter.praktikum-services.ru/"
    ORDER_URL = "https://qa-scooter.praktikum-services.ru/order"
    DZEN_URL = "https://dzen.ru/"

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            print(f'Элемент с локатором {locator} не найден спустя {timeout} секунд')
            return None

    def scroll_to_element(self, locator, timeout=5):
        element = self.find_element(locator, timeout)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        else:
            print(f'Не получилось проскроллить до элемента с локатором {locator}')
            return None

    def click_element(self, locator, timeout=5):
        element = self.find_element(locator, timeout)
        if element:
            element.click()
        else:
            print(f'Не получилось кликнуть по элементу с локатором {locator}')

    def enter_text(self, locator, text, timeout=5):
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            print(f'Ошибка при попытке ввода текста в элемент с локатором {locator}')

    def wait_for_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            print(f'Элемент с локатором {locator} не найден спустя {timeout} секунд')
            return None

    def wait_for_title(self, title, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.title_contains(title))
        except TimeoutException:
            print(f'Страница с title "{title}" не открылась спустя {timeout} секунд')
            return None

    def element_is_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
            return True
        except TimeoutException:
            print(f'Элемент с локатором {locator} не найден спустя {timeout} секунд')
            return None

    @allure.step('Открываем главную страницу')
    def open_main_url(self):
        self.navigate(self.MAIN_URL)

    @allure.step('Открываем страницу заказа самоката')
    def open_order_url(self):
        self.navigate(self.ORDER_URL)

    @allure.step('Кликаем на кнопку "Принять куки", если она есть')
    def click_accept_cookie_button(self):
        self.click_element(self._ACCEPT_COOKIE_BUTTON, 1)

    @allure.step('Кликаем на лого самоката')
    def click_scooter_logo(self):
        self.click_element(self._SCOOTER_LOGO)

    @allure.step('Кликаем на лого Яндекса')
    def click_yandex_logo(self):
        self.click_element(self._YANDEX_LOGO)

    @allure.step('Переключаемся на открывшуюся вкладку')
    def switch_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получаем URL текущей вкладки')
    def get_current_url(self):
        return self.driver.current_url
