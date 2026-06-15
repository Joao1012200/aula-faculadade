# ============================================================
# Exercicio 05 - Maior ou Menor de Idade
# ============================================================
# Enunciado:
#   Leia a idade de uma pessoa e informe se ela e
#   menor de idade ou maior de idade.
#
# Conceitos praticados:
#   - Condicional simples (if / else)
#   - Comparacao com valor limite (18 anos)
# ============================================================

# Passo 1: Ler a idade
idade = int(input("Digite sua idade: "))

# Passo 2: Verificar maioridade (18 anos e o limite no Brasil)
if idade >= 18:
    print("Voce e MAIOR de idade")
else:
    print("Voce e MENOR de idade")
