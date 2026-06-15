media = 0
qtde = 0
soma = 0
nota = float(input("Digite a nota do aluno: "))

while (nota > 0.0):
    soma = soma + nota
    qtde = qtde + 1

    nota = float(input("Digite a nota do aluno: "))

media = soma / qtde
print("\n Total da soma: ", soma)
print("\n Quantidade de notas digitadas: ", qtde)
print("\n Média dos valores: ", media)