A = float(input("Informe um numero: "))
B = float(input("Informe outro numero: "))
C = float(input("Informe outro numero: "))

if A > B and A > C:
    print("O maior numero é:", A)
elif B > A and B > C:
    print("O maior numero é:", B)
else:
    print("O maior numero é:", C)