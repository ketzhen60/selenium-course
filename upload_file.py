import os
from selenium import webdriver

wd = webdriver.Chrome()
wd.get('http://suninjuly.github.io/file_input.html')
wd.find_element_by_name('firstname').send_keys('Name')
wd.find_element_by_name('lastname').send_keys('LastName')
wd.find_element_by_name('email').send_keys('mail@mail.ru')
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла
wd.find_element_by_id('file').send_keys(file_path)
wd.find_element_by_class_name('btn').click()