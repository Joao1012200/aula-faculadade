# ============================================================
# Exercicio 13 - Calculadora Simples
# ============================================================
# Enunciado:
#   Leia dois numeros e uma operacao (+, -, *, /)
#   e calcule o resultado.
#
# Conceitos praticados:
#   - Multiplas condicoes (if / elif)
#   - Cuidado com divisao por zero!
# ============================================================

# Passo 1: Ler os dois numeros e a operacao
a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))
operacao = input("Digite a operacao (+, -, *, /): ")

# Passo 2: Realizar o calculo conforme a operacao escolhida
if operacao == "+":
    resultado = a + b
    print(f"{a} + {b} = {resultado}")

elif operacao == "-":
    resultado = a - b
    print(f"{a} - {b} = {resultado}")

elif operacao == "*":
    resultado = a * b
    print(f"{a} * {b} = {resultado}")

elif operacao == "/":
    # Cuidado! Divisao por zero causa erro
    if b != 0:
        resultado = a / b
        print(f"{a} / {b} = {resultado}")
    else:
        print("ERRO: Divisao por zero nao e permitida!")

else:
    print("Operacao invalida! Use +, -, * ou /")
