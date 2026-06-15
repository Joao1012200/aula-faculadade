# ============================================================
# Exercicio 37 - Simulacao de Votacao
# ============================================================
# Enunciado:
#   Simule uma votacao:
#   - 1 = candidato A
#   - 2 = candidato B
#   - 0 = encerrar votacao
#   - mostrar vencedor ao final
#
# Conceitos praticados:
#   - Contadores por candidato
#   - Validacao de entrada (votos invalidos)
#   - Comparacao final para determinar vencedor
# ============================================================

# Passo 1: Inicializar os contadores
votos_a = 0
votos_b = 0
votos_invalidos = 0

# Passo 2: Menu de votacao
print("=== SISTEMA DE VOTACAO ===")
print("1 - Candidato A")
print("2 - Candidato B")
print("0 - Encerrar votacao")

# Passo 3: Ler os votos
voto = int(input("\nDigite seu voto: "))

while voto != 0:
    if voto == 1:
        votos_a += 1
    elif voto == 2:
        votos_b += 1
    else:
        votos_invalidos += 1
        print("Voto INVALIDO!")

    voto = int(input("Digite seu voto: "))

# Passo 4: Mostrar os resultados
total = votos_a + votos_b + votos_invalidos
print("\n=== RESULTADO ===")
print(f"Candidato A: {votos_a} voto(s)")
print(f"Candidato B: {votos_b} voto(s)")
print(f"Votos invalidos: {votos_invalidos}")
print(f"Total de votos: {total}")

# Passo 5: Determinar o vencedor
if votos_a > votos_b:
    print("\nVENCEDOR: Candidato A!")
elif votos_b > votos_a:
    print("\nVENCEDOR: Candidato B!")
else:
    print("\nEMPATE!")
