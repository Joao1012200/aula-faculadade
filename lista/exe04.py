n1 = int(input("digite um numero: "))
n2 = int(input("digite outro numero: "))
dif = 0

if n1 > n2:
    dif = n1 - n2
    print("Essa é a diferença: %d", dif)
elif n1 == n2:
    dif = 0
    print("O resultado é 0")
else:
    print("Essa é a diferença: %d", dif)