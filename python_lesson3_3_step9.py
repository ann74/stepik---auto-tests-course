import pytest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()

def test_exception():
    browser.get("http://selenium1py.pythonanywhere.com/")
    with pytest.raises(NoSuchElementException, message="Не должно быть кнопки Отправить"):
        browser.find_element_by_css_selector("button.btn")
