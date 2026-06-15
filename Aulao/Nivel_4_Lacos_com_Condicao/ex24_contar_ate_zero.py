# ============================================================
# Exercicio 24 - Contar numeros ate digitar 0
# ============================================================
# Enunciado:
#   Conte quantos numeros foram digitados ate o usuario
#   digitar 0.
#
# Conceitos praticados:
#   - Variavel CONTADORA (conta quantos)
#   - Diferenca entre acumulador (soma valores) e
#     contador (conta quantidades)
# ============================================================

# Passo 1: Inicializar o contador
quantidade = 0

# Passo 2: Ler o primeiro numero
numero = int(input("Digite um numero (0 para sair): "))

# Passo 3: Enquanto nao for 0, conta
while numero != 0:
    quantidade = quantidade + 1  # ou: quantidade += 1
    numero = int(input("Digite um numero (0 para sair): "))

# Passo 4: Mostrar quantos numeros foram digitados
print(f"Voce digitou {quantidade} numero(s) antes do zero.")
