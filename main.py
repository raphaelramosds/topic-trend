import sys
sys.path.append("/topic-trend/modules/")

from modules import services
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Iteração com o usuário
topic = input("Em qual tópico você está interessado?")
days = int(input("Quantos dias atrás?"))
pages = int(input("Deseja que eu pesquise até qual página?"))

# Ir ao Google News
browser = webdriver.Chrome()
browser.get("https://news.google.com/topstories?hl=pt-BR&gl=BR&ceid=BR:pt-419")

# Pesquisar tópico
search_field = browser.find_element_by_xpath("//*[@id='gb']/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]")
search_field.send_keys(topic)
search_field.send_keys(Keys.ENTER)

# Recuperar titulos e tempo de cada notícia
data = []

for i in range(pages):

  # Pegar as informações
  card_periods = browser.find_elements_by_css_selector("g-card > div > div > a > div > div.iRPxbe > div.ZE0LJd > p > span")
  card_titles = browser.find_elements_by_css_selector("g-card > div > div > a > div > div.iRPxbe > div.mCBkyc.y355M.JQe2Ld.nDgy9d")
  n = len(card_titles)

  # Percorrer os titulos individualmente
  for j in range(n):
    title = card_titles[i].text
    period = card_periods[i].text
    news = {}

    # Aplique as regras definidas
    if services.title_has_names(topic, title) and services.period_has_days(period):
      news["title"] = title
      news["period"] = period
      data.append(news)

  # Role até o final da página
  browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  # Clique no próximo item
  browser.find_element_by_css_selector("#pnnext > span:nth-child(2)").click()

# Fechar o navegador
browser.close()

print(data)