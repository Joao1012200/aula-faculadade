n1 = 0

for i in range(5):
    n2 = float(input("Informe um numero: "))
    if n2 > n1:
        n1 = n2

print("O maior número é:", n1)