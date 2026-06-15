#Faça um programa em Python que receba uma lista com 10 valores inteiros
#e mostre para o usuário qual número é o maior e qual é o menor.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(10):
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]

print(f"maior = {maior} e menor = {menor}")