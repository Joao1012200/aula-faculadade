n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe outro número inteiro: "))
diferenca = 0

if n1 > n2:
    diferenca = n1 - n2
    print(f"A diferença entre {n1} e {n2} é : {diferenca}")
elif n1 < n2:
    diferenca = n2 - n1
    print(f"A diferença entre {n2} e {n1} é : {diferenca}")
else:
    print("A diferença é 0")