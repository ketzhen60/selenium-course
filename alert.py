from selenium import webdriver
import math
import calculatefunc

wd = webdriver.Chrome()
wd.get('http://suninjuly.github.io/alert_accept.html')
btn = wd.find_element_by_class_name('btn')
btn.click()
wd.switch_to.alert.accept()
x = int(wd.find_element_by_id('input_value').text)
wd.find_element_by_id('answer').send_keys(calculatefunc.lncalculate(x))
btn = wd.find_element_by_class_name('btn')
btn.click()
