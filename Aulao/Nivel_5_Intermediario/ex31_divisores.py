# ============================================================
# Exercicio 31 - Contar Divisores
# ============================================================
# Enunciado:
#   Leia um numero e conte quantos divisores ele possui.
#
# O que e um divisor?
#   Um divisor de N e um numero que divide N sem deixar resto.
#   Exemplo: divisores de 12 -> 1, 2, 3, 4, 6, 12 (6 divisores)
#
# Conceitos praticados:
#   - Laco for percorrendo de 1 ate N
#   - Operador modulo (%) para verificar divisibilidade
#   - Contador
# ============================================================

# Passo 1: Ler o numero
numero = int(input("Digite um numero: "))

# Passo 2: Inicializar o contador de divisores
quantidade = 0

# Passo 3: Testar cada numero de 1 ate o numero
print(f"Divisores de {numero}:")
for i in range(1, numero + 1):
    if numero % i == 0:  # Se o resto e 0, i e divisor!
        print(i, end=" ")  # end=" " imprime na mesma linha
        quantidade += 1

# Passo 4: Mostrar a quantidade total
print(f"\nTotal de divisores: {quantidade}")
