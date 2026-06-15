# ============================================================
# Exercicio 34 - Jogo de Adivinhacao
# ============================================================
# Enunciado:
#   Jogo de adivinhacao:
#   - numero fixo (ex: 7)
#   - usuario tenta ate acertar
#   - diga se o chute e maior ou menor que o numero secreto
#
# Conceitos praticados:
#   - While com condicao de acerto
#   - Dicas ao usuario (maior/menor)
#   - Contador de tentativas
# ============================================================

# Passo 1: Definir o numero secreto
numero_secreto = 7

# Passo 2: Inicializar contador de tentativas
tentativas = 0

print("=== JOGO DE ADIVINHACAO ===")
print("Estou pensando em um numero de 1 a 10...")

# Passo 3: Ler o primeiro chute
chute = int(input("Seu chute: "))
tentativas += 1

# Passo 4: Repetir ate acertar, dando dicas
while chute != numero_secreto:
    # Dar dica para o usuario
    if chute > numero_secreto:
        print("O numero secreto e MENOR!")
    else:
        print("O numero secreto e MAIOR!")

    chute = int(input("Tente novamente: "))
    tentativas += 1

# Passo 5: Acertou! Saiu do laco
print(f"\nPARABENS! Voce acertou em {tentativas} tentativa(s)!")
