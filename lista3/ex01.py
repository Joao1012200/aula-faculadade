aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"O {aluno} foi aprovado com média {media}")
elif media <= 5:
    print(f"O {aluno} foi reprovado com media {media}")
else:
    print(f"O {aluno} ficou em recuperação com media {media}")