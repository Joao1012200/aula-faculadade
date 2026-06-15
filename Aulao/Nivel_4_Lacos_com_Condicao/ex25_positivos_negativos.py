# ============================================================
# Exercicio 25 - Contar Positivos e Negativos
# ============================================================
# Enunciado:
#   Leia varios numeros ate 0 e informe:
#   - quantos sao positivos
#   - quantos sao negativos
#
# Conceitos praticados:
#   - Dois contadores independentes
#   - Condicional DENTRO do laco
# ============================================================

# Passo 1: Inicializar os contadores
positivos = 0
negativos = 0

# Passo 2: Ler o primeiro numero
numero = int(input("Digite um numero (0 para sair): "))

# Passo 3: Laco com contagem condicional
while numero != 0:
    if numero > 0:
        positivos += 1  # Conta positivo
    else:
        negativos += 1  # Conta negativo (numero < 0, pois != 0 ja foi filtrado)

    numero = int(input("Digite um numero (0 para sair): "))

# Passo 4: Mostrar os resultados
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
