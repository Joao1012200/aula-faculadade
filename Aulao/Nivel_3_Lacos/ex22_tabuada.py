# ============================================================
# Exercicio 22 - Tabuada
# ============================================================
# Enunciado:
#   Leia um numero e mostre sua tabuada (de 1 a 10).
#   Exemplo: numero = 5
#     5 x 1 = 5
#     5 x 2 = 10
#     ...
#     5 x 10 = 50
#
# Conceitos praticados:
#   - Laco for
#   - Operador de multiplicacao (*)
#   - f-string para formatacao
# ============================================================

# Passo 1: Ler o numero
numero = int(input("Digite um numero para ver a tabuada: "))

# Passo 2: Mostrar a tabuada de 1 a 10
print(f"\n--- Tabuada do {numero} ---")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
