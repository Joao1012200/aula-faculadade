#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e
#mostre a soma dos quadrados dos elementos do vetor.

vetor = []

for i in range(10):
    numero = int(input("Digite um numero: "))
    vetor.append(numero)

print(f"Soma dos quadrados dos numeros: {sum(x**2 for x in vetor)}")