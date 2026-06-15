A = float(input("Informe um numero: "))
B = float(input("Informe um numero: "))
C = float(input("Informe um numero: "))

if A > B and A > C:
    if B > C:
        ordem = C, B, A
    else:
        ordem = B, C, A
elif B > A and B > C:
    if A > C:
        ordem = C, A, B
    else:
        ordem = A, C, B
elif C > A and C > B:
    if A > B:
        ordem = B, A, C
    else:
        ordem = A, B, C

print("A ordem decrescente é: ", ordem)
