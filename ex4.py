def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def menu(operacao):
    if operacao == "+":
        return somar(a, b)
    elif operacao == "-":
        return subtrair(a, b)
    elif operacao == "*":
        return multiplicar(a, b)
    elif operacao == "/":
        return dividir(a, b)
    else:
        return print("operacao invalida")

while True:
    a = int(input("Informe um numero:"))
    b = int(input("Informe outro numero:"))
    operacao = input("Informe a operacao (+, -, *, /):")
    if operacao not in ["+", "-", "*", "/"]:
        break
    print(menu(operacao))