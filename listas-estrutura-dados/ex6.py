#Faça um programa que leia 20 números inteiros e armazene-os num vetor.
#Armazene os números pares no vetor PAR e os números IMPARES no vetor
#impar. Imprima os três vetores.

numeros = []
pares = []
impares = []

for i in range(20):
    numero = int(input("Digite um numero: "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Os numeros digitados foram: {numeros}")
print(f"Os numeros pares digitados foram: {pares}")
print(f"Os numeros impares digitados foram: {impares}")