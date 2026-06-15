#Faça um programa que leia 4 notas, mostre as notas e a média na tela.



notas = []
soma = 0

for i in range(4):
    nota = float(input("Digite a nota: "))
    notas.append(nota)
    soma += nota
    media = soma / 4

print(f"As notas do aluno foi: {notas}\nA media das notas foi: {media:.2f}")