aluno = str(input("Digite o nome do aluno: "))
sexo = str(input("Digite o sexo do aluno [F/M]: ")).upper()
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if sexo == "M" or sexo == "F":
    if media >= 6 and sexo == "M":
        print(f"Caro {aluno} seu resultado é: {media}, voce foi aprovado")
    elif media >= 6 and sexo == "F":
        print(f"Cara {aluno} seu resultado é: {media}, voce foi aprovada")
    else:
        if media < 6 and sexo == "M":
            print(f"Caro {aluno} seu resultado é: {media}, voce foi reprovado")
        else:
            print(f"Cara {aluno} seu resultado é: {media}, voce foi reprovada")