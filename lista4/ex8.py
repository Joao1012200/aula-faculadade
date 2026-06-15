n = int(input("Informe um numero: "))

if n > 0:
    for i in range(0, n + 1):
        print(f"o dobro de {i} é {i*2}")
else:
    print("informe um numero inteiro menor que 0")