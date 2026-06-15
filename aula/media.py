notaA = float(input("Digite a primeira nota: "))
notaB = float(input("Digite a segunda nota: "))

media = (notaA + notaB)/2
if media >= 6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print("O aluno está :", situacao)
