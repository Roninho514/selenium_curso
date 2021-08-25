from selenium.webdriver import Chrome

Chrome = Chrome()
Chrome.get('http://selenium.dunossauro.live/aula_05_a.html')
python = Chrome.find_element_by_id('python')
haskell = Chrome.find_element_by_id('haskell')
print(python.text)
print(haskell.text)
Chrome.quit()
