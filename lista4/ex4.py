n1 = int(input("informe um numero: "))
n2 = int(input("informe outro numero: "))

for i in range(n1, n2 + 1):
    if i % 2 == 1:
        print(i)