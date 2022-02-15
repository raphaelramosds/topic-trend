from selenium import webdriver
from selenium.webdriver.common.keys import  Keys

# Ir ao google.com
browser = webdriver.Chrome()
browser.get("http://www.google.com/")

# Pesquisar tópico
topic = "monark nazismo"

search_field = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search_field.send_keys(topic)
search_field.send_keys(Keys.ENTER)

# Ir para a página de notícias
news_btn = browser.find_element_by_xpath("//*[@id='hdtb-msb']/div[1]/div/div[4]/a")
news_btn.click()

# Pegar cards das notícias g-card[class=ftSUBd]
