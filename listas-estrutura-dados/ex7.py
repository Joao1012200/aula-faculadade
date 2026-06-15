#Faça um programa que peça as quatro notas de 10 alunos, calcule e
#armazene num vetor a média de cada aluno, imprima o número de alunos
#com média maior ou igual a 7.0.



medias = []
alunos_aprovados = []
alunos = [
    "Ana Clara",
    "Bruno Silva",
    "Carla Mendes",
    "Diego Santos",
    "Fernanda Costa",
    "Gabriel Oliveira",
    "Helena Rocha",
    "Igor Almeida",
    "Juliana Martins",
    "Lucas Pereira"
]
contador = 0

def media(nota1, nota2, nota3, nota4):
    return (nota1 + nota2 + nota3 + nota4) / 4


for i in range(10):
    print(f"Aluno: {alunos[i]} informa as notas:")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    nota4 = float(input("Digite a nota 4: "))
    medias.append(media(nota1, nota2, nota3, nota4))

    if media(nota1, nota2, nota3, nota4) >= 7:
        alunos_aprovados.append(alunos[i])
        contador += 1

print(f"Total de alunos aprovados: {contador} sao eles: {alunos_aprovados} Parabens!!")




