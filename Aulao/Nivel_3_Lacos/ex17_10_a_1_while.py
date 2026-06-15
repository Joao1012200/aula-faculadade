# ============================================================
# Exercicio 17 - Numeros de 10 a 1 com WHILE
# ============================================================
# Enunciado:
#   Mostre os numeros de 10 a 1 usando while.
#
# Conceitos praticados:
#   - Laco while (repete ENQUANTO a condicao for verdadeira)
#   - Variavel de controle (contador)
#   - Decrementar o contador a cada volta
# ============================================================

# Passo 1: Inicializar o contador
contador = 10

# Passo 2: Enquanto o contador for >= 1, continua repetindo
while contador >= 1:
    print(contador)
    # Passo 3: Diminuir o contador (MUITO IMPORTANTE!)
    # Sem isso, o laco nunca para -> laco infinito!
    contador = contador - 1  # ou: contador -= 1
