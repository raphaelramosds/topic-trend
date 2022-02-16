import time
from datetime import datetime

# Verifica se as palavras do tópico estão inclusas no título da notícia
def title_has_names(topic, title):

  keywords = topic.split()
  occurrences = []
  n = len(keywords)

  # Colocar titulo da noticia em lowercase
  title = title.casefold()

  # Pesquisar ocorrências
  for i in range(n):

    # Hipótese: a palavra está (valor 1)
    occurrences.append(1)
    if title.find(keywords[i]) < 0:
      occurrences[i] = 0

  # Caso o maior valor seja zero, não houve nenhuma ocorrência
  return False if max(occurrences) == 0 else True

# Extrair a data das publicações
def extract_date_from(period):

  # Separe a data
  array = period.split("T")
  str_date = array[0]

  return str_date
