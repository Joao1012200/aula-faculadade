# ============================================================
# Exercicio 30 - Sequencia de Fibonacci (10 primeiros)
# ============================================================
# Enunciado:
#   Gere os 10 primeiros numeros da sequencia de Fibonacci.
#
# O que e Fibonacci?
#   Cada numero e a soma dos dois anteriores:
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Como funciona:
#   a = 0, b = 1
#   proximo = a + b = 1
#   depois: a vira b, b vira proximo
#   e repete!
#
# Conceitos praticados:
#   - Duas variaveis que se "empurram"
#   - Laco for com quantidade fixa
# ============================================================

# Passo 1: Definir os dois primeiros termos
a = 0  # primeiro termo
b = 1  # segundo termo

# Passo 2: Mostrar os 10 primeiros termos
print("Os 10 primeiros numeros de Fibonacci:")

for i in range(10):
    print(a)  # Mostra o termo atual

    # Passo 3: Calcular o proximo termo
    # O proximo e a soma dos dois anteriores
    proximo = a + b

    # Passo 4: "Empurrar" os valores
    # a recebe o valor de b
    # b recebe o proximo
    a = b
    b = proximo

    # Visualizacao do que acontece a cada volta:
    # Volta 0: a=0, b=1 -> mostra 0, proximo=1 -> a=1, b=1
    # Volta 1: a=1, b=1 -> mostra 1, proximo=2 -> a=1, b=2
    # Volta 2: a=1, b=2 -> mostra 1, proximo=3 -> a=2, b=3
    # Volta 3: a=2, b=3 -> mostra 2, proximo=5 -> a=3, b=5
    # ...
