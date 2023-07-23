import allure
import pytest

from pages.main_page import MainPage
from test_data.data import Titles


class TestMainPage:

    @allure.title('Подтвержение куки на странице')
    def test_accept_cookies(self, setup):
        main_page = MainPage(setup)
        main_page.accept_cookies()

    @allure.title('Проверка перехода на страницу Яндекс.Дзен по нажатию на лого Яндекса')
    def test_transition_to_dzen_main_page(self, setup):
        main_page = MainPage(setup)
        main_page.click_on_yandex_logo()
        main_page.check_transition_to_dzen_main_page()

    @allure.title('Проверка перехода на главную старницу по нажатию на лого Самоката')
    def test_transition_to_scooter_main_page(self, setup):
        main_page = MainPage(setup)
        main_page.click_on_scooter_logo()
        main_page.check_transition_to_scooter_main_page(Titles.HEADER_TEXT)

    @allure.title('Проверка соответствия вопроса-ответа в блоке "Вопросы о важном"')
    @pytest.mark.parametrize('num', [i for i in range(8)])
    def test_answers_on_important_questions(self, setup, num):
        main_page = MainPage(setup)
        main_page.get_list_of_questions_on_important_question(num)
        main_page.get_list_of_answers()
        main_page.check_answers_on_questions(num)

