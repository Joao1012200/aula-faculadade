# ============================================================
# Exercicio 18 - Numeros pares de 1 a 20
# ============================================================
# Enunciado:
#   Mostre todos os numeros pares de 1 a 20.
#
# Conceitos praticados:
#   - Laco for com range
#   - Condicional dentro do laco
#   - OU uso do range com passo (step)
# ============================================================

# --- Forma 1: for com if (mais didatica) ---
print("Forma 1 (for + if):")
for i in range(1, 21):
    if i % 2 == 0:  # Se o resto da divisao por 2 for 0, e par
        print(i)

# --- Forma 2: range com passo de 2 (mais eficiente) ---
print("\nForma 2 (range com passo):")
# range(2, 21, 2) -> comeca em 2, vai ate 20, pulando de 2 em 2
for i in range(2, 21, 2):
    print(i)
