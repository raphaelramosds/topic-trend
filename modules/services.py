# Verifica se as palavras do tópico estão inclusas no título da notícia

def title_has_names(topic, title):

  keywords = topic.split()
  occurrences = []
  n = len(keywords)

  # Colocar titulo da noticia em lowercase
  title = title.casefold()

  # Pesquisar ocorrências
  for i in range(n):
    occurrences.append(1) # Hipótese: a palavra está (valor 1)
    if title.find(keywords[i]) < 0:
      occurrences[i] = 0

  # Caso o maior valor seja zero, não houve nenhuma ocorrência
  return False if max(occurrences) == 0 else True

print(title_has_names("monark nazismo partido", "Em defesa de Kataguiri, MBL recorda fala de Lula sobre Hitler"))