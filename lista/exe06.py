n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
sexo = str(input("Digite o sexo [M/F]: ")).upper()

media = (n1 + n2 + n3 + n4) / 4

if media >= 6:
    if sexo == "M":
        print(f"Caro aluno, seu resultado é: {media} aprovado")
    else:
        print(f"Cara aluna, seu resultado é {media} aprovada")
else:
    if sexo == "M":
        print(f"Caro aluno, seu resultado é {media} reprovado")
    else:
        print(f"Cara aluna, seu resultado é {media} reprovada")