from selenium import webdriver
import math
import calculatefunc
import time

wd = webdriver.Chrome()
wd.get('http://suninjuly.github.io/redirect_accept.html')
wd.find_element_by_class_name('btn').click()
wd.switch_to.window(wd.window_handles[1])
x = int(wd.find_element_by_id('input_value').text)
wd.find_element_by_class_name('form-control').send_keys(calculatefunc.lncalculate(x))
wd.find_element_by_class_name('btn').click()
time.sleep(4)
wd.quit()
