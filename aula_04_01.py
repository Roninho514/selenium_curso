from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://selenium.dunossauro.live/aula_04_a.html')
tabela = browser.find_element_by_tag_name('ul')
lis = tabela.find_elements_by_tag_name('li')
lis[0].find_element_by_tag_name('a').text

