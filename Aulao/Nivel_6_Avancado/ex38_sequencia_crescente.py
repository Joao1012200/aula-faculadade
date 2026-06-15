# ============================================================
# Exercicio 38 - Verificar Sequencia Crescente
# ============================================================
# Enunciado:
#   Leia N numeros e verifique se a sequencia esta crescente.
#   Exemplo crescente: 2, 5, 8, 10 -> SIM
#   Exemplo nao crescente: 2, 5, 3, 10 -> NAO (5 > 3)
#
# Estrategia:
#   Comparar cada numero com o anterior.
#   Se algum for MENOR que o anterior, nao e crescente.
#
# Conceitos praticados:
#   - Guardar o valor anterior para comparacao
#   - Flag (bandeira) de controle
# ============================================================

# Passo 1: Ler a quantidade de numeros
n = int(input("Quantos numeros voce vai digitar? "))

# Passo 2: Ler o primeiro numero
anterior = int(input("Digite o 1o numero: "))

# Passo 3: Assumir que e crescente ate provar o contrario
crescente = True

# Passo 4: Ler os demais e comparar com o anterior
for i in range(2, n + 1):
    atual = int(input(f"Digite o {i}o numero: "))

    # Se o atual for MENOR ou IGUAL ao anterior, nao e crescente
    if atual <= anterior:
        crescente = False
        # Poderiamos usar break aqui, mas vamos ler todos

    # O atual vira o "anterior" para a proxima volta
    anterior = atual

# Passo 5: Mostrar resultado
if crescente:
    print("\nA sequencia e CRESCENTE!")
else:
    print("\nA sequencia NAO e crescente.")
