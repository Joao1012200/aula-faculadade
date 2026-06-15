qtde = int(input("Informe a quantidade de alunos: "))
aluno = 0
aluno_maior = 0
idade = 0
cont = 0
soma = 0
nota = 0
nota_maior = -1
media = 0
aprovado = 0

for i in range(1, qtde + 1):
    aluno = str(input("Digite o nome do aluno: "))
    cont += 1
    idade = int(input("Digite a idade: "))
    nota = float(input("Digite a nota: "))
    if idade > 0 and nota >= 0:
        soma +=nota
        media = soma / cont
        if nota >= 6:
            aprovado += 1
            if nota > nota_maior:
                nota_maior = nota
                aluno_maior = aluno

print(f"A media dos alunos foi de {media}"
      f"\nForam aprovados {aprovado} alunos"
      f"\nO maior nota foi {nota_maior} do aluno {aluno_maior}")