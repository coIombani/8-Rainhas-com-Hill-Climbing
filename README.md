# 8 rainhas com Hill Climbing

Trabalho de Sistemas Inteligentes feito em Python. Busca uma posição para oito rainhas sem ataques entre elas, usando Hill Climbing com reinícios aleatórios.

Cada coluna tem uma rainha. A cada passo, o algoritmo escolhe o movimento que mais reduz os conflitos de linha e diagonal. Se não houver melhora, começa outra tentativa com um tabuleiro aleatório, até o limite de 100 tentativas.

## Como executar

Com Python 3 instalado, execute na pasta do projeto:

```bash
python 8_Rainhas.py
```

Não precisa instalar bibliotecas externas. O programa imprime o tabuleiro, os conflitos, os passos e o tempo da busca. A solução pode mudar a cada execução, e nem toda execução encontra uma solução dentro do limite.