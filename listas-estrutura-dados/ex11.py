#Faça um programa que leia dois vetores com 10 elementos cada. Gere um
#terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
#elementos intercalados dos dois outros vetores.

vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
vetor3 = []

for i in range(20):
    vetor3.append(vetor1[i % 10])
    vetor3.append(vetor2[i % 10])

print(vetor3)