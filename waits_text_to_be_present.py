from selenium import webdriver
import calculatefunc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wd = webdriver.Chrome()
wd.get('http://suninjuly.github.io/explicit_wait2.html')
button = wd.find_element_by_id('book')
WebDriverWait(wd, 5).until(EC.text_to_be_present_in_element((By.ID, "price"),'100'))
button.click()
x = int(wd.find_element_by_id('input_value').text)
wd.find_element_by_id('answer').send_keys(calculatefunc.lncalculate(x))
btn = wd.find_element_by_id('solve')
btn.click()