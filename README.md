Тестирование учебного сервиса «Яндекс.Самокат»

1. Фреймворк selenium
2. Браузер - Firefox 
3. Команда для запуска всех тестов — pytest -v tests 
4. Генерация отчетов Allure: pytest --alluredir=allure_results 
5. Для формирования отчета в формате веб-страницы: allure serve allure_results

 Описание тестов: 
1. test_main_page.py - проверка переходов по логотипам, проверка соответствия вопросов-ответов в блоке "Вопросы о важном"
2. test_order_page.py - проверка формы заказа самоката 