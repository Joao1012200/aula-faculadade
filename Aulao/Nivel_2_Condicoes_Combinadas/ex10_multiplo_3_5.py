# ============================================================
# Exercicio 10 - Multiplo de 3, de 5 ou de ambos
# ============================================================
# Enunciado:
#   Leia um numero e verifique se ele e:
#   - multiplo de 3
#   - multiplo de 5
#   - multiplo de ambos (3 e 5)
#
# Conceitos praticados:
#   - Operador modulo (%)
#   - Operador logico "and"
#   - IMPORTANTE: testar "ambos" PRIMEIRO (ordem dos ifs importa!)
# ============================================================

# Passo 1: Ler o numero
numero = int(input("Digite um numero: "))

# Passo 2: Verificar multiplos
# ATENCAO: verificamos "ambos" primeiro!
# Se verificarmos "multiplo de 3" antes, o numero 15 cairia ali
# e nunca chegaria na verificacao de "ambos"
if numero % 3 == 0 and numero % 5 == 0:
    print(f"{numero} e multiplo de 3 E de 5")
elif numero % 3 == 0:
    print(f"{numero} e multiplo de 3")
elif numero % 5 == 0:
    print(f"{numero} e multiplo de 5")
else:
    print(f"{numero} NAO e multiplo de 3 nem de 5")
