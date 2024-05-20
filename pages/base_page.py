import allure
from selenium.webdriver.common.by import By


class BasePage:

    _ACCEPT_COOKIE_BUTTON = [By.XPATH, "//button[contains(@class,'App_CookieButton')]"]
    _SCOOTER_LOGO = [By.XPATH, "//a[contains(@class, 'LogoScooter')]"]
    _YANDEX_LOGO = [By.XPATH, "//a[contains(@class, 'LogoYandex')]"]

    MAIN_URL = "https://qa-scooter.praktikum-services.ru/"
    ORDER_URL = "https://qa-scooter.praktikum-services.ru/order"
    DZEN_URL = "https://dzen.ru/"

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем главную страницу')
    def open_main_url(self):
        self.driver.get(self.MAIN_URL)

    @allure.step('Открываем страницу заказа самоката')
    def open_order_url(self):
        self.driver.get(self.ORDER_URL)

    @allure.step('Кликаем на кнопку "Принять куки", если она есть')
    def click_accept_cookie_button(self):
        try:
            return self.driver.find_element(*self._ACCEPT_COOKIE_BUTTON).click()
        except Exception:
            return None

    @allure.step('Кликаем на лого самоката')
    def click_scooter_logo(self):
        self.driver.find_element(*self._SCOOTER_LOGO).click()

    @allure.step('Кликаем на лого Яндекса')
    def click_yandex_logo(self):
        self.driver.find_element(*self._YANDEX_LOGO).click()

    @allure.step('Переключаемся на открывшуюся вкладку и получаем ее URL')
    def get_new_tab_url(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.driver.current_url
