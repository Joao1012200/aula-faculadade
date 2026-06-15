n = int(input("insira um numero maior que zero: "))

while n <= 0:
    print("número invalido, insira um numero válido")
    n = int(input("insira um numero maior que zero: "))

soma = 0
contador = n - 1

while contador > 0:
    soma += contador
    contador -= 1

print(f"A soma dos números anteriores a {n} é {soma}")
