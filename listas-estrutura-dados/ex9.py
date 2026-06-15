#Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada
#informação no seu respectivo vetor. Imprima a idade e a altura na ordem
#inversa à ordem lida.

idades = []
alturas = []


for i in range(5):
    idade = int(input(f"Digite a idade da {i+1} pessoa: "))
    altura = float(input(f"Digite a altura da {i+1} pessoa: "))
    idades.append(idade)
    alturas.append(altura)

print("\nIdades na ordem inversa: ", idades[::-1])
print("Alturas na ordem inversa: ", alturas[::-1], "\n")