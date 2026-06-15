def somar_numeros(a, b):
    return a + b

def subtrair_numeros(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
operacao = input("Escolha a operação (+ , -, *, /)")

if operacao == "+":
    resultado = somar_numeros(a, b)
elif operacao == "-":
    resultado = subtrair_numeros(a, b)
elif operacao == "*":
    resultado = multiplicar(a, b)
else:
    resultado = dividir(a, b)

print(resultado)
