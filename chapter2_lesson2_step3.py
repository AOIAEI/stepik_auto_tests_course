from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element_by_id("num1")
    a = a_element.text
    b_element = browser.find_element_by_id("num2")
    b = b_element.text
    y = int(a)+int(b)
    
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(y))
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

