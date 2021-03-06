# Sistema
import time
import sys
sys.path.append("/topic-trend/modules/")

# Módulos adicionais
from modules import handling
import pandas as pd

# Webscraping
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Iteração com o usuário
topic = input("Em qual tópico você está interessado? ")

# Ir ao Google Notícias
browser = webdriver.Chrome()
browser.get("https://news.google.com/topstories?hl=pt-BR&gl=BR&ceid=BR:pt-419")

# Pesquisar tópico
search_field = browser.find_element_by_xpath("//*[@id='gb']/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]")
search_field.send_keys(topic)
search_field.send_keys(Keys.ENTER)

# Recuperar titulos e tempo de cada notícia
data = {}

data["period"] = []
data["title"] = []

# Esperar a página carregar
time.sleep(2)

# Role até o final da página n vezes
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Pegar as informações
prefix = "#yDmH0d > c-wiz > div > div.FVeGwb.CVnAc.Haq2Hf.bWfURe > div.ajwQHc.BL5WZb.RELBvb > div > main > c-wiz > div.lBwEZb.BL5WZb.xP6mwf > div > div > article"
card_periods = browser.find_elements_by_css_selector(f"{prefix} > div > div > time")
card_titles = browser.find_elements_by_css_selector(f"{prefix} > h3")
n = min(len(card_periods), len(card_titles))

# Percorrer os titulos individualmente
for j in range(n):

  # Definição dos titulos e tempos da publicação
  title = card_titles[j].text
  period = card_periods[j].get_attribute("datetime")

  # Aplique as regras definidas
  if handling.title_has_names(topic, title):
    data["title"].append(title)
    data["period"].append(handling.extract_date_from(period))

# Fechar o navegador
browser.close()

# Exportar dados
table = pd.DataFrame(data)
table.to_csv("./assets/news.csv", index=False)