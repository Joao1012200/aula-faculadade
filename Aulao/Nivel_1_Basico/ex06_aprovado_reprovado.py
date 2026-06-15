# ============================================================
# Exercicio 06 - Aprovado ou Reprovado
# ============================================================
# Enunciado:
#   Leia uma nota (0 a 10) e informe se o aluno esta
#   aprovado (>= 7) ou reprovado (< 7).
#
# Conceitos praticados:
#   - Entrada com float (nota pode ter decimal, ex: 6.5)
#   - Condicional simples
# ============================================================

# Passo 1: Ler a nota (usamos float pois nota pode ser 7.5, etc)
nota = float(input("Digite a nota (0 a 10): "))

# Passo 2: Verificar aprovacao
if nota >= 7:
    print("APROVADO!")
else:
    print("REPROVADO!")
