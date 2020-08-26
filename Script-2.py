from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
x = int(browser.find_element_by_id('input_value').text)
y = math.log(abs(12*math.sin(x)))
browser.find_element_by_id('answer').send_keys(str(y))
button = browser.find_element_by_tag_name("button")
#прокрутка к элементу
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
browser.find_element_by_id('robotCheckbox').click()
browser.find_element_by_id('robotsRule').click()
button.click()
time.sleep(3)
browser.quit()

assert True