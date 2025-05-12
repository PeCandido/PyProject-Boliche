# 🎳 Sistema de Pontuação de Boliche (Python + Docker)
Este projeto implementa a lógica de pontuação de um jogo de boliche em Python. Ele lê uma sequência de jogadas e calcula a pontuação total, exibindo também os frames do jogo.

## 📦 Requisitos para o Docker
- [Docker](https://www.docker.com/) instalado na máquina.

## 🚀 Como executar com Docker
1. **Clone este repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. **Construa a imagem Docker:**
   " docker build -t boliche . "

3. **Execute o container:**
   " docker run -it boliche "

## Entrada e Saída
O projeto pede uma entrada de valores inteiros que ditam a pontuação em cada jogada, separado por espaço
O programa terá como saída os frames do jogo e a pontuação total ao final

Exemplo de entrada: 
10 9 1 5 5 7 2 10 10 10 9 0 8 2 9 1 10

Saída esperada: 
X _ | 9 / | 5 / | 7 2 | X _ | X _ | X _ | 9 0 | 8 / | 9 / X
187
