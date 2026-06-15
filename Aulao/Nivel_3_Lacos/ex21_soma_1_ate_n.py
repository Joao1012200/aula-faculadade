# ============================================================
# Exercicio 21 - Soma de 1 ate N
# ============================================================
# Enunciado:
#   Leia um numero N e calcule a soma de 1 ate N.
#   Exemplo: N = 5 -> 1 + 2 + 3 + 4 + 5 = 15
#
# Conceitos praticados:
#   - Variavel ACUMULADORA (soma)
#   - Padrao: inicializar com 0 e ir somando a cada volta
# ============================================================

# Passo 1: Ler o valor de N
n = int(input("Digite um numero N: "))

# Passo 2: Inicializar o acumulador com 0
soma = 0

# Passo 3: Somar cada numero de 1 ate N
for i in range(1, n + 1):
    soma = soma + i  # ou: soma += i
    # Descomente a linha abaixo para ver o passo a passo:
    # print(f"  somei {i}, soma parcial = {soma}")

# Passo 4: Mostrar o resultado
print(f"A soma de 1 ate {n} e: {soma}")
