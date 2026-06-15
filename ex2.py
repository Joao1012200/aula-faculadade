def maior(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

def menor(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

a = int(input("Informe um numero:"))
b = int(input("Informe outro numero:"))
c = int(input("Informe mais um numero:"))
print("O maior é: ", maior(a,b,c))
print("O menor é: ", menor(a,b,c))