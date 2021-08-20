from selenium import webdriver
from time import sleep
from pprint import pprint
from urllib.parse import urlparse

browser = webdriver.Chrome()
browser.get('http://selenium.dunossauro.live/aula_04.html')
sleep(3)
def get_link(browser,tag_location):
    tag = browser.find_element_by_tag_name(tag_location)
    tag_links = tag.find_elements_by_tag_name('a')
    resultado = {}
    for element in tag_links:
        resultado[element.text] = element.get_attribute('href')
    return resultado

links_aulas = get_link(browser, 'aside')

exercicios_links = get_link(browser, 'main')
browser.get(exercicios_links['Exercício 3'])
sleep(2)
clicar = get_link(browser, 'main')
browser.get(clicar['Começar por aqui'])
sleep(2)
clicar = browser.find_elements_by_tag_name('a')
for click in clicar:
    link = click.get_attribute('href')
    if (link == 'https://selenium.dunossauro.live/page_2.html'):
        certo = click
certo.click()
sleep(3)
browser.refresh()
sleep(2)
browser.refresh()
sleep(4)
titulo_pagina = browser.title
print(titulo_pagina)
clicar = browser.find_elements_by_tag_name('a')
for click in clicar:
    texto = click.text
    if (texto == titulo_pagina):
        certo = click
certo.click()
sleep(3)
url_parcelada = urlparse(browser.current_url)
url_parcelada = url_parcelada.path
print(url_parcelada)
clicar = browser.find_elements_by_tag_name('a')
for click in clicar:
    if click.text == url_parcelada[1:]:
        certo = click
certo.click()
sleep(2)
browser.refresh()
