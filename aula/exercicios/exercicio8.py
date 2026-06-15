A = float(input("Informe um numero: "))
B = float(input("Informe outro numero: "))
C = float(input("Informe outro numero: "))

if A > B and A > C:
    maior = A
    if B < C:
        menor = B
    else:
        menor = C
elif B > A and B > C:
    maior = B
    if A < C:
        menor = A
    else:
        menor = C
elif C > A and C > B:
    maior = C
    if A < B:
        menor = A
    else:
        menor = B

print("O maior é", maior, "O menor é", menor)