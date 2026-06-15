# ============================================================
# Exercicio 03 - Par ou Impar
# ============================================================
# Enunciado:
#   Leia um numero e verifique se ele e par ou impar.
#
# Conceitos praticados:
#   - Operador modulo (%) -> retorna o resto da divisao
#   - Se o resto da divisao por 2 for 0, o numero e par
# ============================================================

# Passo 1: Ler o numero
numero = int(input("Digite um numero: "))

# Passo 2: Verificar usando o operador % (modulo/resto)
# Exemplo: 4 % 2 = 0 (par) | 5 % 2 = 1 (impar)
if numero % 2 == 0:
    print(f"{numero} e PAR")
else:
    print(f"{numero} e IMPAR")
