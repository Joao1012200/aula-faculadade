# ============================================================
# Exercicio 04 - Maior entre tres numeros
# ============================================================
# Enunciado:
#   Leia tres numeros e mostre o maior deles.
#
# Conceitos praticados:
#   - Comparacao encadeada com if / elif / else
#   - Operador logico "and" para combinar condicoes
# ============================================================

# Passo 1: Ler os tres numeros
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

# Passo 2: Comparar para encontrar o maior
# Para "a" ser o maior, ele precisa ser >= b E >= c
if a >= b and a >= c:
    print(f"O maior e {a}")
elif b >= a and b >= c:
    print(f"O maior e {b}")
else:
    print(f"O maior e {c}")
