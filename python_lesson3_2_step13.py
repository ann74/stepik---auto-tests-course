from selenium import webdriver
import time
import unittest
import os.path

options = webdriver.ChromeOptions()
options.add_argument("--enable-features=NetworkServiceWindowsSandbox")
options.add_argument("--disable-features=NetworkService")
browser = webdriver.Chrome(chrome_options=options)

def registration(link):
    browser.get(link)
    input1 = browser.find_element_by_css_selector(".first_block .first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".first_block .second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".first_block .third")
    input3.send_keys("test@mail.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    return welcome_text_elt.text

class TestRegistr(unittest.TestCase):
    def test_registr1(self):
        text_registration = registration("http://suninjuly.github.io/registration1.html")
        self.assertEqual(text_registration, "Поздравляем! Вы успешно зарегистировались!")

    def test_registr2(self):
        text_registration = registration("http://suninjuly.github.io/registration2.html")
        self.assertEqual(text_registration, "Поздравляем! Вы успешно зарегистировались!")
        
if __name__ == "__main__":
    unittest.main()
