# ============================================================
# Exercicio 26 - Maior numero digitado
# ============================================================
# Enunciado:
#   Leia numeros ate 0 e mostre o maior numero digitado.
#
# Conceitos praticados:
#   - Variavel para guardar o "maior ate agora"
#   - Tecnica: inicializar com o PRIMEIRO valor lido
#   - Atualizar quando encontrar um valor maior
# ============================================================

# Passo 1: Ler o primeiro numero
numero = int(input("Digite um numero (0 para sair): "))

# Passo 2: O primeiro numero digitado e, por enquanto, o maior
maior = numero

# Passo 3: Continuar lendo e comparando
while numero != 0:
    if numero > maior:
        maior = numero  # Encontrou um novo maior!

    numero = int(input("Digite um numero (0 para sair): "))

# Passo 4: Mostrar o maior
if maior != 0:
    print(f"O maior numero digitado foi: {maior}")
else:
    print("Nenhum numero foi digitado antes do zero.")
