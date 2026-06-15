n = 0
soma = 0

for i in range(1, 6):
    n = int(input("Digite um numero: "))
    soma += n

if soma % 2 == 0:
    print(f"A soma dos numeros é: {soma}, logo é um numero par")
else:
    print(f"A soma dos numeros é: {soma}, logo é um numero impar")


