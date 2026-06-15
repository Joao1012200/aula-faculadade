# ============================================================
# Exercicio 02 - Maior entre dois numeros
# ============================================================
# Enunciado:
#   Leia dois numeros e informe qual e o maior.
#
# Conceitos praticados:
#   - Entrada de dados
#   - Comparacao entre valores
#   - Estrutura condicional (if / elif / else)
# ============================================================

# Passo 1: Ler os dois numeros
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))

# Passo 2: Comparar os dois numeros
if a > b:
    print(f"O maior e {a}")
elif b > a:
    print(f"O maior e {b}")
else:
    print("Os números são iguais")
