# ============================================================
# Exercicio 19 - Numeros impares de 1 a 20
# ============================================================
# Enunciado:
#   Mostre todos os numeros impares de 1 a 20.
#
# Conceitos praticados:
#   - Mesma logica do ex18, mas agora com impares
#   - range com passo comecando de 1
# ============================================================

# --- Forma 1: for com if ---
print("Forma 1 (for + if):")
for i in range(1, 21):
    if i % 2 != 0:  # Se o resto NAO for 0, e impar
        print(i)

# --- Forma 2: range com passo de 2, comecando em 1 ---
print("\nForma 2 (range com passo):")
# range(1, 21, 2) -> 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
for i in range(1, 21, 2):
    print(i)
