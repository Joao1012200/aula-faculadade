n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))

n3 = n1 + 1

for i in range(n3, n2):
    if i % 2 == 0:
        print(i)