#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que
#determine quantos alunos com mais de 13 anos possuem altura inferior à
#média de altura desses alunos.

idades = []
alturas = []

for i in range(30):
    idade = int(input("Digite a idade do aluno: "))
    altura = float(input("Digite a altura do aluno: "))
    idades.append(idade)
    alturas.append(altura)

media_altura = sum(alturas) / len(alturas)

contador = 0
for i in range(30):
    if idades[i] > 13 and alturas[i] < media_altura:
        contador += 1

print(f"\n{contador} alunos com mais de 13 anos e altura inferior a media:")