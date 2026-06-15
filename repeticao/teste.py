n = int(input("informe um numero inteiro: "))

if n <= 0:
    print("valor invalido")
else:
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b
        print()