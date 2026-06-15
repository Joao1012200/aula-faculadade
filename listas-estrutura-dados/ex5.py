#Faça um programa que leia um vetor de 10 caracteres, e diga quantas
#consoantes foram lidas. Imprima as consoantes.



caracteres = []
consoantes = []
vogais = ['a', 'e', 'i', 'o', 'u']

for i in range(10):
    caracter = input(f"Digite o {i+1} caracter: ").lower()

    if caracter not in vogais:
        consoantes.append(caracter)

    caracteres.append(caracter)

print(f"Consoantes: {len(consoantes)}")
print("Consoantes lidas: ", consoantes)
print("Todos caracteres digitados: ", caracteres)