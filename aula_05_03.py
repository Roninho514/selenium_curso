from selenium.webdriver import Chrome
from time import sleep

Chrome = Chrome()
Chrome.get('http://selenium.dunossauro.live/aula_05_c.html')
def melhor_filmin(browser,filme,email,telefone):
    browser.find_element_by_name('filme').send_keys(filme)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('enviar').click()
melhor_filmin(Chrome,'parasita','emailfake@gmail.com','(032)46244932')
sleep(2)
Chrome.quit()