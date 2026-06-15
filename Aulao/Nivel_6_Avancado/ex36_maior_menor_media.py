# ============================================================
# Exercicio 36 - Maior, Menor e Media
# ============================================================
# Enunciado:
#   Leia numeros ate 0 e informe:
#   - maior
#   - menor
#   - media
#
# Conceitos praticados:
#   - Combinar TUDO que aprendemos:
#     acumulador, contador, maior, menor
#   - Inicializar maior/menor com o primeiro valor lido
# ============================================================

# Passo 1: Ler o primeiro numero
numero = float(input("Digite um numero (0 para sair): "))

# Passo 2: Verificar se ja comecou com 0
if numero == 0:
    print("Nenhum numero foi digitado!")
else:
    # Passo 3: Inicializar todas as variaveis com o primeiro valor
    maior = numero
    menor = numero
    soma = numero
    quantidade = 1

    # Passo 4: Ler os proximos numeros
    numero = float(input("Digite um numero (0 para sair): "))

    while numero != 0:
        # Atualizar maior
        if numero > maior:
            maior = numero

        # Atualizar menor
        if numero < menor:
            menor = numero

        # Acumular soma e contar
        soma += numero
        quantidade += 1

        numero = float(input("Digite um numero (0 para sair): "))

    # Passo 5: Mostrar os resultados
    media = soma / quantidade
    print(f"\nMaior: {maior}")
    print(f"Menor: {menor}")
    print(f"Media: {media:.2f}")
