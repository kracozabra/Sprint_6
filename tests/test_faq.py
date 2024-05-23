import allure
import pytest
from pages.main_page import MainPage
from data import faq_tab_data


class TestFaq:

    @allure.title('Проверка вопросов и ответов в блоке "FAQ"')
    @pytest.mark.parametrize('tab_number,question,answer', faq_tab_data)
    def test_faq(self, driver, tab_number, question, answer):
        main_page = MainPage(driver)
        main_page.open_main_url()
        main_page.wait_for_load_faq_section()
        main_page.scroll_to_faq_section()
        main_page.click_question_tab(tab_number)
        actual_question_text = main_page.get_question_text(tab_number)
        actual_answer_text = main_page.get_answer_text(tab_number)

        assert actual_answer_text == answer and actual_question_text == question, 'Текст вопроса или ответа не соответвует требуемому значению'
