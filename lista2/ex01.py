n = int(input("Informe um número maior que zero: "))
soma = 0

if n > 0:
    for i in range(1, n):
        soma += i

    print(f"A soma é {soma}")
else:
    print("Informe um número maior que zero")