# ============================================================
# Exercicio 01 - Positivo, Negativo ou Zero
# ============================================================
# Enunciado:
#   Leia um numero e informe se ele e positivo, negativo ou zero.
#
# Conceitos praticados:
#   - Entrada de dados (input)
#   - Conversao de tipo (int)
#   - Estrutura condicional (if / elif / else)
# ============================================================

# Passo 1: Ler o numero digitado pelo usuario
numero = int(input("Digite um numero: "))

# Passo 2: Verificar se e positivo, negativo ou zero
if numero > 0:
    print("O numero e POSITIVO")
elif numero < 0:
    print("O numero e NEGATIVO")
else:
    print("O numero e ZERO")
