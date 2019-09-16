from selenium import webdriver
import time
import math

# задание: заполнить поле, выбрать необходимые чекбоксы и радиобаттон и нажать кнопку Submit, проскроллив экран с огромным футером
# Подробнее: https://stepik.org/lesson/228249/step/6?unit=200781

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value")
    x = x.text
    y = calc(x)
 
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    button = browser.find_element_by_css_selector("button.btn.btn-primary")
   # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.execute_script("window.scrollBy(0, 50);")

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    browser.execute_script("window.scrollBy(0,50);")
    button.click()

finally:
    time.sleep(30)
    browser.quit()