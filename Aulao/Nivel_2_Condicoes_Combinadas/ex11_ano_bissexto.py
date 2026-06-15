# ============================================================
# Exercicio 11 - Ano Bissexto
# ============================================================
# Enunciado:
#   Leia um ano e verifique se e bissexto.
#
# Regra do ano bissexto:
#   Um ano e bissexto se:
#     - E divisivel por 4
#     - MAS se for divisivel por 100, NAO e bissexto
#     - EXCETO se tambem for divisivel por 400, ai E bissexto
#
# Exemplos:
#   2024 -> bissexto (divisivel por 4, nao por 100)
#   1900 -> NAO bissexto (divisivel por 100, mas nao por 400)
#   2000 -> bissexto (divisivel por 400)
#
# Conceitos praticados:
#   - Condicoes compostas com "and" e "or"
#   - Logica mais elaborada
# ============================================================

# Passo 1: Ler o ano
ano = int(input("Digite um ano: "))

# Passo 2: Aplicar a regra do ano bissexto
# Forma simplificada da regra:
# Bissexto se (divisivel por 4 E nao por 100) OU (divisivel por 400)
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} e um ano BISSEXTO")
else:
    print(f"{ano} NAO e um ano bissexto")
