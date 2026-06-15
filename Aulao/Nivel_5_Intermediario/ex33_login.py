# ============================================================
# Exercicio 33 - Sistema de Login
# ============================================================
# Enunciado:
#   Simule um sistema de login:
#   - usuario e senha corretos definidos no codigo
#   - repetir ate o usuario acertar
#
# Conceitos praticados:
#   - While com condicao baseada em acerto
#   - Comparacao de strings
#   - Operador logico "or" (basta UM estar errado)
# ============================================================

# Passo 1: Definir o usuario e senha corretos
usuario_correto = "admin"
senha_correta = "1234"

# Passo 2: Ler a primeira tentativa
print("=== SISTEMA DE LOGIN ===")
usuario = input("Usuario: ")
senha = input("Senha: ")

# Passo 3: Repetir enquanto estiver errado
# O laco continua enquanto usuario OU senha estiverem errados
while usuario != usuario_correto or senha != senha_correta:
    print("\nUsuario ou senha INCORRETOS! Tente novamente.\n")
    usuario = input("Usuario: ")
    senha = input("Senha: ")

# Passo 4: Se saiu do laco, e porque acertou!
print("\nLogin realizado com SUCESSO! Bem-vindo!")
