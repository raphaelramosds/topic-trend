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

# Apenas permite notícias que possuam "(há) dias (atrás)"
def period_has_days(period):
  return True if period.find("dias") > 0 or period.find("dia") > 0 else False