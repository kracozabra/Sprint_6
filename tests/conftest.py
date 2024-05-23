import pytest
from selenium import webdriver


# Помогает корректно выводить символы кириллицы в консоли PyCharm
def pytest_make_parametrize_id(config, val):
    return repr(val)


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
