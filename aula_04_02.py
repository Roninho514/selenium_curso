from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://selenium.dunossauro.live/aula_04_a.html')


def encontra_texto_elemento(browser, tag, texto):
    elementos = browser.find_elements_by_tag_name(tag)
    for elemento in elementos:
        if texto in elemento.text:
            return elemento


def encontra_link_elemento(browser, tag, link):
    elementos = browser.find_elements_by_tag_name(tag)
    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento


elemento = encontra_texto_elemento(browser, 'li', 'DuckDuckGo').text
print(elemento)
link = encontra_link_elemento(browser,'a','ddg.gg').get_attribute('href')
print(link)
