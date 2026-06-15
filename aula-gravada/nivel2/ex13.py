a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))
operacao = input("Digite a operação (+, -, *, /)")

if operacao == "+":
    result = a + b
    print(f"{a} + {b} = {result}")
elif operacao == "-":
    result = a - b
    print(f"{a} - {b} = {result}")
elif operacao == "*":
    result = a * b
    print(f"{a} * {b} = {result}")
elif operacao == "/":
    if a != 0:
        result = a / b
        print(f"{a} / {b} = {result}")
    else:
        print("ERRO: divisão por 0 não é permitido")
else:
    print("Operação invalida")