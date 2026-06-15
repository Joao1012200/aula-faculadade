#Faça um programa que leia um vetor de 5 números inteiros, mostre a soma,
#a multiplicação e os números.

numeros = []

def soma(a, b, c, d, e):
    return a + b + c + d + e

def multiplo(a, b, c, d, e):
    return a * b * c * d * e

for i in range(5):
    numeros.append(int(input("Digite um numero: ")))

soma_numeros = soma(*numeros)
multiplo_numeros = multiplo(*numeros)

print(f"Os numeros digitados foram: {numeros} \nSoma dos numeros: {soma_numeros} \nMultiplo dos numeros: {multiplo_numeros}")