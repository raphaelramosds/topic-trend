# Tendência de um tópico

A ideia principal é que possamos avaliar a relevância de um determinado tópico a partir das datas de publicações de notícias relacionados a ele.

![](./carbon.png)

### Regras de negócio

`at least one keyword` caso nenhuma palavra chave do tópico esteja no título da notícia, ela não será considerada

`34NT2020/04/12 should be 2020-04-12` o tempo de publicação da notícia deve estar no formato %y-%m-%d
