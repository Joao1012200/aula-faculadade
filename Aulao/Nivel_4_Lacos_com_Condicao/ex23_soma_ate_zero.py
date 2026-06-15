# ============================================================
# Exercicio 23 - Soma ate digitar 0
# ============================================================
# Enunciado:
#   Leia numeros ate o usuario digitar 0. Mostre a soma.
#
# Conceitos praticados:
#   - Laco while com condicao de parada
#   - Variavel acumuladora
#   - "Sentinela" -> valor especial que encerra o laco (0)
# ============================================================

# Passo 1: Inicializar o acumulador
soma = 0

# Passo 2: Ler o primeiro numero
numero = int(input("Digite um numero (0 para sair): "))

# Passo 3: Enquanto NAO for 0, continua somando
while numero != 0:
    soma = soma + numero  # Acumula o valor
    numero = int(input("Digite um numero (0 para sair): "))  # Le o proximo

# Passo 4: Mostrar a soma total
print(f"A soma total e: {soma}")
