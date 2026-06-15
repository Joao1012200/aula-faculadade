# ============================================================
# Exercicio 09 - Menor entre tres numeros
# ============================================================
# Enunciado:
#   Leia tres numeros e mostre o menor.
#
# Conceitos praticados:
#   - Mesma logica do ex04, mas agora buscando o MENOR
#   - Operador logico "and"
# ============================================================

# Passo 1: Ler os tres numeros
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

# Passo 2: Encontrar o menor
# Para "a" ser o menor, ele precisa ser <= b E <= c
if a <= b and a <= c:
    print(f"O menor e {a}")
elif b <= a and b <= c:
    print(f"O menor e {b}")
else:
    print(f"O menor e {c}")
