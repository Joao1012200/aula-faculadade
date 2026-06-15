# ============================================================
# Exercicio 39 - Contar Positivos antes do Primeiro Negativo
# ============================================================
# Enunciado:
#   Leia numeros ate encontrar um negativo:
#   - conte quantos foram positivos antes disso
#
# Conceitos praticados:
#   - While com condicao composta
#   - Parada ao encontrar condicao especifica
# ============================================================

# Passo 1: Inicializar o contador
positivos = 0

# Passo 2: Ler o primeiro numero
numero = int(input("Digite um numero: "))

# Passo 3: Enquanto o numero for positivo ou zero, continua
while numero >= 0:
    if numero > 0:
        positivos += 1
    # Nota: se for 0, nao conta como positivo nem negativo

    numero = int(input("Digite um numero: "))

# Passo 4: Saiu do laco porque encontrou um negativo
print(f"\nNumero negativo encontrado: {numero}")
print(f"Quantidade de positivos antes dele: {positivos}")
