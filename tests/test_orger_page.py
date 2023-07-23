import allure
import pytest

from pages.order_page import OrderPage
from test_data.data import Urls, UserInfo, Titles, IncorrectUser


class TestOrderPage:

    @allure.title('Заказ самоката по кнопке "Заказать" вверху страницы')
    def test_order_from_button_in_header(self, setup):
        order_page = OrderPage(setup)
        order_page.click_on_order_button_in_header()
        order_page.fill_info_about_customer(UserInfo.NAME, UserInfo.LAST_NAME, UserInfo.ADDRESS, UserInfo.METRO[0], UserInfo.PHONE_NUMBER)
        order_page.click_on_next_button()
        order_page.fill_rent_info(UserInfo.DATE_OF_ORDER[0], UserInfo.RENT_PERIOD[0], UserInfo.COMMENT)
        order_page.click_on_order_button()
        order_page.approve_order()
        order_page.check_success_order(Titles.SUCCESSFUL_ORDER)

    @allure.title('Заказ самоката по кнопке "Заказать" внизу страницы')
    def test_order_in_bottom(self, setup):
        order_page = OrderPage(setup)
        order_page.click_on_order_button_in_header()
        order_page.fill_info_about_customer(UserInfo.NAME, UserInfo.LAST_NAME, UserInfo.ADDRESS, UserInfo.METRO[1], UserInfo.PHONE_NUMBER)
        order_page.click_on_next_button()
        order_page.fill_rent_info(UserInfo.DATE_OF_ORDER[1], UserInfo.RENT_PERIOD[1], UserInfo.COMMENT)
        order_page.click_on_order_button()
        order_page.approve_order()
        order_page.check_success_order(Titles.SUCCESSFUL_ORDER)

    @allure.title('Заказ самоката по прямой ссылке')
    def test_fill_info_about_order(self, setup):
        order_page = OrderPage(setup)
        order_page.go_to_url(Urls.ORDER_URL)
        order_page.click_on_order_button_in_header()
        order_page.fill_info_about_customer(UserInfo.NAME, UserInfo.LAST_NAME, UserInfo.ADDRESS, UserInfo.METRO[2], UserInfo.PHONE_NUMBER)
        order_page.click_on_next_button()
        order_page.fill_rent_info(UserInfo.DATE_OF_ORDER[2], UserInfo.RENT_PERIOD[2], UserInfo.COMMENT)
        order_page.click_on_order_button()
        order_page.approve_order()
        order_page.check_success_order(Titles.SUCCESSFUL_ORDER)

    @allure.title('Проверка заказа самоката с некорректными данными')
    @pytest.mark.parametrize('name, last_name, address, phone, error_message',
                             (IncorrectUser.NAME, IncorrectUser.LAST_NAME, IncorrectUser.ADDRESS, IncorrectUser.PHONE),
                             ids=['incorrect_name', 'incorrect_last_name', 'incorrect_address', 'incorrect_phone'])
    def test_fill_incorrect_data_in_(self, setup, name, last_name, address, phone, error_message):
        order_page = OrderPage(setup)
        order_page.go_to_url(Urls.ORDER_URL)
        order_page.click_on_order_button_in_header()
        order_page.fill_info_about_customer(name, last_name, address, UserInfo.METRO[0], phone)
        order_page.check_warning_message(error_message)
