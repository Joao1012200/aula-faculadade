# ============================================================
# Exercicio 14 - Classificacao por Faixa Etaria
# ============================================================
# Enunciado:
#   Leia uma idade e classifique:
#   - crianca (0 a 12)
#   - adolescente (13 a 17)
#   - adulto (18 a 59)
#   - idoso (60+)
#
# Conceitos praticados:
#   - Multiplos elif (varios intervalos)
#   - A ORDEM dos testes importa!
# ============================================================

# Passo 1: Ler a idade
idade = int(input("Digite a idade: "))

# Passo 2: Classificar por faixa etaria
# Como testamos em ordem crescente, cada elif ja
# "sabe" que os anteriores falharam
if idade < 0:
    print("Idade invalida!")
elif idade <= 12:
    # Se chegou aqui, idade >= 0 (pois o if acima nao pegou)
    print("Crianca")
elif idade <= 17:
    # Se chegou aqui, idade >= 13 (pois o elif acima nao pegou)
    print("Adolescente")
elif idade <= 59:
    # Se chegou aqui, idade >= 18
    print("Adulto")
else:
    # Se chegou aqui, idade >= 60
    print("Idoso")
