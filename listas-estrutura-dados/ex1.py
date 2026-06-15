#Faça um programa que leia um vetor de 5 números inteiros e mostre-os.

numeros = []

for i in range(5):
    valor = int(input("Digite um valor: "))
    numeros.append(valor)

print("Os numeros digitados foram: ")
for i in numeros:
    print(i)