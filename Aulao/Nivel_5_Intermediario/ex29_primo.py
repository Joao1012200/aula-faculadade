# ============================================================
# Exercicio 29 - Verificar se e Primo
# ============================================================
# Enunciado:
#   Leia um numero e verifique se ele e primo.
#
# O que e um numero primo?
#   E um numero maior que 1 que so e divisivel por 1 e por
#   ele mesmo. Exemplos: 2, 3, 5, 7, 11, 13, 17, 19, 23...
#
# Estrategia:
#   Tentar dividir o numero por todos os valores de 2 ate
#   numero-1. Se nenhum dividir exato, e primo.
#
# Conceitos praticados:
#   - Laco for com break
#   - Variavel "flag" (bandeira) para sinalizar resultado
# ============================================================

# Passo 1: Ler o numero
numero = int(input("Digite um numero: "))

# Passo 2: Tratar casos especiais
if numero <= 1:
    print(f"{numero} NAO e primo")
else:
    # Passo 3: Assumir que e primo ate provar o contrario
    eh_primo = True  # "flag" = bandeira de controle

    # Passo 4: Tentar dividir por cada numero de 2 ate numero-1
    for i in range(2, numero):
        if numero % i == 0:
            # Encontrou um divisor! Entao NAO e primo
            eh_primo = False
            break  # Nao precisa continuar testando

    # Passo 5: Mostrar resultado
    if eh_primo:
        print(f"{numero} e PRIMO!")
    else:
        print(f"{numero} NAO e primo (e divisivel por {i})")
