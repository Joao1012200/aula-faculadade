# ============================================================
# Exercicio 27 - Contar pares entre 10 numeros
# ============================================================
# Enunciado:
#   Leia 10 numeros e conte quantos sao pares.
#
# Conceitos praticados:
#   - Laco for com quantidade FIXA de repeticoes
#   - Contador condicional (so conta se for par)
# ============================================================

# Passo 1: Inicializar o contador de pares
pares = 0

# Passo 2: Repetir 10 vezes (for com range)
for i in range(1, 11):
    numero = int(input(f"Digite o {i}o numero: "))

    # Passo 3: Verificar se e par e contar
    if numero % 2 == 0:
        pares += 1

# Passo 4: Mostrar o resultado
print(f"\nDos 10 numeros digitados, {pares} sao pares.")
