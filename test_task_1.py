"""
С использованием Selenium Webdriver, применяя паттерн проектирования Page Object и сохраняя веб-локаторы 
в отдельном yaml-файле выполнить следующие тесты в браузере Google Chrome: 
- логин на сайт 
- клик по ссылке About 
- проверка, что шрифт в заголовке открывшегося окна имеет размер 32 px.
"""

import logging
from testpage import OperationsHelper
import yaml
import pytest



with open('testdata.yaml',encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_task_1(browser):
    logging.info("Task 1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    testpage.click_about()
    assert testpage.about_text() == "32px"
