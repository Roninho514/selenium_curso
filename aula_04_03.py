from selenium import webdriver
from time import  sleep

browser = webdriver.Chrome()
browser.get('http://selenium.dunossauro.live/aula_04_b.html')

def encontra_texto_elemento(browser, tag, texto):
    elementos = browser.find_elements_by_tag_name(tag)
    for elemento in elementos:
        if elemento.text == texto:
            return elemento
numeros = ['um','dois','tres','quatro']
for numero in numeros:
    encontra_texto_elemento(browser, 'div', numero).click()
    sleep(0.3)

for numero in numeros:
    browser.back()
    sleep(0.3)

for numero in numeros:
    browser.forward()
    sleep(0.3)
