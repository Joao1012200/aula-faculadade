#Faça um programa que leia um vetor de 10 números reais e mostre-os na
#ordem inversa.

lista = []

for i in range(10):
    lista.append(int(input("Digite um valor: ")))
    lista.insert(0, lista.pop())

print(lista)