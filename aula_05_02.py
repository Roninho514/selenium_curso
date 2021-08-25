from selenium.webdriver import Chrome

Chrome = Chrome()
Chrome.get('http://selenium.dunossauro.live/aula_05_b.html')
topicos = Chrome.find_elements_by_class_name('topico')
linguagens = Chrome.find_elements_by_class_name('linguagens')
for linguagem in linguagens:
    print((linguagem.find_element_by_tag_name('h2').text,
    linguagem.find_element_by_tag_name('p').text))
