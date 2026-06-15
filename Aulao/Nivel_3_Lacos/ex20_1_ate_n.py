# ============================================================
# Exercicio 20 - Mostrar de 1 ate N
# ============================================================
# Enunciado:
#   Leia um numero N e mostre de 1 ate N.
#
# Conceitos praticados:
#   - Usar o valor digitado pelo usuario no range
#   - Lembrar: range(1, N+1) para incluir o N
# ============================================================

# Passo 1: Ler o valor de N
n = int(input("Digite um numero N: "))

# Passo 2: Mostrar de 1 ate N
# range(1, n+1) -> precisamos do +1 porque range nao inclui o ultimo
for i in range(1, n + 1):
    print(i)
