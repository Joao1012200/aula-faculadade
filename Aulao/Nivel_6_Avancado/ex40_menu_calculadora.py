# ============================================================
# Exercicio 40 - Menu de Calculadora
# ============================================================
# Enunciado:
#   Simule um menu:
#   - 1: soma
#   - 2: subtracao
#   - 3: sair
#   - repetir ate o usuario escolher sair
#
# Conceitos praticados:
#   - Laco while True com break (padrao de menu)
#   - Estrutura de menu interativo
#   - Combina tudo: laco + condicional + entrada/saida
# ============================================================

# O laco while True roda "para sempre"
# So para quando encontra um "break"
while True:
    # Passo 1: Mostrar o menu
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Sair")

    # Passo 2: Ler a opcao do usuario
    opcao = int(input("Escolha uma opcao: "))

    # Passo 3: Processar a opcao escolhida
    if opcao == 1:
        # SOMA
        a = float(input("Digite o primeiro numero: "))
        b = float(input("Digite o segundo numero: "))
        resultado = a + b
        print(f"Resultado: {a} + {b} = {resultado}")

    elif opcao == 2:
        # SUBTRACAO
        a = float(input("Digite o primeiro numero: "))
        b = float(input("Digite o segundo numero: "))
        resultado = a - b
        print(f"Resultado: {a} - {b} = {resultado}")

    elif opcao == 3:
        # SAIR
        print("Saindo... Ate mais!")
        break  # Encerra o laco while True

    else:
        # Opcao invalida
        print("Opcao INVALIDA! Escolha 1, 2 ou 3.")
