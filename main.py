import sys
sys.path.append("/topic-trend/modules/")

from modules import services
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

topic = input("Em qual tópico você está interessado?")
days = int(input("Quantos dias atrás?"))
pages = int(input("Deseja que eu pesquise até qual página?"))

services.title_has_name(topic)

# Ir ao google.com
browser = webdriver.Chrome()
browser.get("http://www.google.com/")

# Pesquisar tópico
search_field = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search_field.send_keys(topic)
search_field.send_keys(Keys.ENTER)

# Ir para a página de notícias
news_btn = browser.find_element_by_xpath("//*[@id='hdtb-msb']/div[1]/div/div[4]/a")
news_btn.click()

# Recuperar titulos e tempo de cada notícia
data = []

for i in range(pages):

  # Pegar as informações
  card_periods = browser.find_elements_by_css_selector("g-card > div > div > a > div > div.iRPxbe > div.ZE0LJd > p > span")
  card_titles = browser.find_elements_by_css_selector("g-card > div > div > a > div > div.iRPxbe > div.mCBkyc.y355M.JQe2Ld.nDgy9d")

  # Role a página
  browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  # Clique no próximo item
  browser.find_element_by_css_selector("#pnnext > span:nth-child(2)").click()

# Fechar o navegador
browser.close()