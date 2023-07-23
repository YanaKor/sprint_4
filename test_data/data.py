from faker import Faker
import random


class Urls:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_URL = 'https://qa-scooter.praktikum-services.ru/order'


class UserInfo:
    fake_ru = Faker('ru_Ru')
    fake_en = Faker('en_US')
    NAME = fake_ru.first_name()
    LAST_NAME = fake_ru.last_name()
    ADDRESS = random.choice(['Москва', 'Московская область']) + ', ' + 'ул. ' + fake_ru.street_name()
    PHONE_NUMBER = random.randint(10000000000, 99999999999)
    COMMENT = str(fake_ru.text())
    METRO = ["Черкизовская", "Сокольники", "Медведково"]
    DATE_OF_ORDER = ['15.08.2023', '14.09.2023', '01.10.2023']
    RENT_PERIOD = ['сутки', 'двое суток', 'пятеро суток']


class Titles:
    HEADER_TEXT = "Самокат\nна пару дней\nПривезём его прямо к вашей двери,\nа когда накатаетесь — заберём"
    SUCCESSFUL_ORDER = 'Заказ оформлен'
    FIRST_NAME_ERROR = 'Введите корректное имя'
    LAST_NAME_ERROR = 'Введите корректную фамилию'
    ADDRESS_ERROR = 'Введите корректный адрес'
    PHONE_NUMBER_ERROR = 'Введите корректный номер'


class Questions:
    LIST_OF_QUESTIONS = [
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        "Пока что у нас так: один заказ — один самокат. "
        "Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
        "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
        "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "Самокат приезжает к вам с полной зарядкой. "
        "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. "
        "Зарядка не понадобится.",
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    ]


class IncorrectUser:
    NAME = ['test', UserInfo.LAST_NAME, UserInfo.ADDRESS, UserInfo.PHONE_NUMBER, Titles.FIRST_NAME_ERROR]
    LAST_NAME = [UserInfo.NAME, 'test', UserInfo.ADDRESS, UserInfo.PHONE_NUMBER, Titles.LAST_NAME_ERROR]
    ADDRESS = [UserInfo.NAME, UserInfo.LAST_NAME, 'test', UserInfo.PHONE_NUMBER, Titles.ADDRESS_ERROR]
    PHONE = [UserInfo.NAME, UserInfo.LAST_NAME, UserInfo.ADDRESS, 'test', Titles.PHONE_NUMBER_ERROR]

