from selenium import webdriver
import math

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("num1")
x = x_element.text
y_element = browser.find_element_by_id("num2")
y = y_element.text
z = str(int(x)+int(y))

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(z)

button = browser.find_element_by_css_selector("button.btn")
button.click()

alert = browser.switch_to.alert
print(alert.text.split()[-1])
alert.accept()

browser.close()
browser.quit()

