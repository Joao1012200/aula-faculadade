# ============================================================
# Exercicio 32 - Media dos numeros digitados
# ============================================================
# Enunciado:
#   Leia varios numeros ate 0 e calcule a media.
#   Media = soma / quantidade
#
# Conceitos praticados:
#   - Acumulador (soma) + Contador (quantidade)
#   - Combinar os dois para calcular a media
#   - Cuidado com divisao por zero (se digitar 0 logo de cara)
# ============================================================

# Passo 1: Inicializar acumulador e contador
soma = 0
quantidade = 0

# Passo 2: Ler o primeiro numero
numero = float(input("Digite um numero (0 para sair): "))

# Passo 3: Laco de leitura
while numero != 0:
    soma += numero       # Acumula o valor
    quantidade += 1      # Conta a quantidade
    numero = float(input("Digite um numero (0 para sair): "))

# Passo 4: Calcular e mostrar a media
if quantidade > 0:
    media = soma / quantidade
    print(f"\nSoma: {soma}")
    print(f"Quantidade: {quantidade}")
    print(f"Media: {media:.2f}")  # :.2f mostra 2 casas decimais
else:
    print("Nenhum numero foi digitado!")
