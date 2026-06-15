# ============================================================
# Exercicio 35 - Caixa Eletronico
# ============================================================
# Enunciado:
#   Simule um caixa eletronico:
#   - Leia o valor a sacar
#   - Informe a quantidade de notas de 100, 50, 20 e 10
#
# Estrategia (algoritmo guloso):
#   Usar o MAXIMO de notas grandes primeiro, depois as menores.
#   Usa divisao inteira (//) e modulo (%)
#
# Exemplo: sacar 380
#   380 // 100 = 3 notas de 100 (sobram 80)
#    80 //  50 = 1 nota de 50   (sobram 30)
#    30 //  20 = 1 nota de 20   (sobram 10)
#    10 //  10 = 1 nota de 10   (sobram 0)
#
# Conceitos praticados:
#   - Divisao inteira (//) e modulo (%)
#   - Algoritmo guloso (greedy)
# ============================================================

# Passo 1: Ler o valor do saque
valor = int(input("Digite o valor do saque (multiplo de 10): "))

# Passo 2: Verificar se e multiplo de 10
if valor % 10 != 0:
    print("ERRO: O valor deve ser multiplo de 10!")
else:
    print(f"\nSaque de R${valor}:")

    # Passo 3: Calcular as notas de 100
    notas_100 = valor // 100     # Quantas notas de 100 cabem?
    valor = valor % 100          # Quanto sobra?

    # Passo 4: Calcular as notas de 50
    notas_50 = valor // 50
    valor = valor % 50

    # Passo 5: Calcular as notas de 20
    notas_20 = valor // 20
    valor = valor % 20

    # Passo 6: Calcular as notas de 10
    notas_10 = valor // 10
    valor = valor % 10

    # Passo 7: Mostrar o resultado
    print(f"  Notas de R$100: {notas_100}")
    print(f"  Notas de R$50:  {notas_50}")
    print(f"  Notas de R$20:  {notas_20}")
    print(f"  Notas de R$10:  {notas_10}")
