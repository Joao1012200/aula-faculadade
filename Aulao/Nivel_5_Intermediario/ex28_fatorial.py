# ============================================================
# Exercicio 28 - Fatorial
# ============================================================
# Enunciado:
#   Calcule o fatorial de um numero.
#
# O que e fatorial?
#   5! = 5 * 4 * 3 * 2 * 1 = 120
#   3! = 3 * 2 * 1 = 6
#   1! = 1
#   0! = 1 (por definicao)
#
# Conceitos praticados:
#   - Variavel acumuladora com MULTIPLICACAO
#   - Inicializar com 1 (nao com 0, senao tudo fica 0!)
# ============================================================

# Passo 1: Ler o numero
n = int(input("Digite um numero: "))

# Passo 2: Inicializar o resultado com 1
# ATENCAO: aqui usamos 1 porque estamos multiplicando!
# Se usassemos 0, qualquer coisa * 0 = 0
fatorial = 1

# Passo 3: Multiplicar de 1 ate N
for i in range(1, n + 1):
    fatorial = fatorial * i  # ou: fatorial *= i
    # Descomente para ver o passo a passo:
    # print(f"  {i}! = {fatorial}")

# Passo 4: Mostrar o resultado
print(f"{n}! = {fatorial}")
