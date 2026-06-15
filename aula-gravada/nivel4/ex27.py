pares = 0

for i in range(1, 11):
    n = int(input(f"Digite o {i} numero"))

    if n % 2 == 0:
        pares += 1

print(f"Dos 10 numeros digitados, {pares} sao pares.")