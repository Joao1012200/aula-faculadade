def maior_entre_tres(a, b, c):
    if a > b and a > c:
        return print(f"o maior é {a}")
    elif b > a and b > c:
        return print(f"o maior é {b}")
    elif c > a and c > b:
        return print(f"o maior é {c}")
    else:
        return print("O ")

a = int(input("Informe um numero: "))
b = int(input("Informe um numero: "))
c = int(input("Informe um numero: "))

print(maior_entre_tres(a, b, c))