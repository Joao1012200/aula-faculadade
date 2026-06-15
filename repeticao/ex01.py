nota1 = 0

for nota1 in range(0, 11):
    nota1 = float(input("Digite uma nota: "))
    if nota1 < 0 or nota1 > 10:
        print("nota invalida")
        continue