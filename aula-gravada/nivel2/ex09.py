n1 = int(input("digite um numero"))
n2 = int(input("digite outro numero"))
n3 = int(input("digite outro numero"))

if n1 < n2 and n1 < n3:
    print(f"O numero menor é: {n1}")
elif n2 < n1 and n2 < n3:
    print(f"O numero menor é: {n2}")
else:
    print(f"o numero menor é: {n3}")