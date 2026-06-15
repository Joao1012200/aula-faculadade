def fatorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

n = int(input("Informe um numero:"))
if n > 0:
    print(f"O fatorial de {n} é: ", fatorial(n))
else:
    print("O numero deve ser maior que 0")