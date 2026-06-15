# ============================================================
# Exercicio 15 - Verificar se forma um Triangulo
# ============================================================
# Enunciado:
#   Leia tres lados e verifique se formam um triangulo.
#
# Regra do triangulo:
#   Tres lados formam um triangulo se CADA lado for MENOR
#   que a soma dos outros dois.
#   |a - b| < c < a + b  (para todos os lados)
#
# Forma simplificada:
#   a < b + c  E  b < a + c  E  c < a + b
#
# Conceitos praticados:
#   - Operador logico "and" com 3 condicoes
#   - Regra matematica aplicada
# ============================================================

# Passo 1: Ler os tres lados
a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

# Passo 2: Verificar a condicao de existencia do triangulo
if a < b + c and b < a + c and c < a + b:
    print("Os lados FORMAM um triangulo!")
else:
    print("Os lados NAO formam um triangulo.")
