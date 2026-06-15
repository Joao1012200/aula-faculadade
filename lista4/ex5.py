n = 0
soma = 0

while n >= 0:
    n = int(input("informe um numero: "))
    if n >= 0:
        soma += n
    else:
        break
print(soma)