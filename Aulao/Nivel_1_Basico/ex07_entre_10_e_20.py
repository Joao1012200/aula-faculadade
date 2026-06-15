# ============================================================
# Exercicio 07 - Numero entre 10 e 20
# ============================================================
# Enunciado:
#   Leia um numero e verifique se ele esta entre 10 e 20.
#
# Conceitos praticados:
#   - Operador logico "and"
#   - Intervalo de valores
# ============================================================

# Passo 1: Ler o numero
numero = int(input("Digite um numero: "))

# Passo 2: Verificar se esta no intervalo [10, 20]
# Precisamos que AMBAS as condicoes sejam verdadeiras:
#   numero >= 10  E  numero <= 20
if numero >= 10 and numero <= 20:
    print(f"{numero} esta entre 10 e 20")
else:
    print(f"{numero} NAO esta entre 10 e 20")
