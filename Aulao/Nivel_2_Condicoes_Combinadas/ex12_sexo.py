# ============================================================
# Exercicio 12 - Sexo (M/F)
# ============================================================
# Enunciado:
#   Leia o sexo (M ou F) e mostre:
#   - Masculino
#   - Feminino
#   - Invalido (se nao for M nem F)
#
# Conceitos praticados:
#   - Entrada de texto (string)
#   - Comparacao de strings
#   - .upper() para aceitar maiuscula e minuscula
# ============================================================

# Passo 1: Ler o sexo
sexo = input("Digite o sexo (M/F): ")

# Passo 2: Converter para maiuscula para aceitar 'm' ou 'M'
sexo = sexo.upper()

# Passo 3: Verificar
if sexo == "M":
    print("Masculino")
elif sexo == "F":
    print("Feminino")
else:
    print("Invalido! Digite apenas M ou F.")
