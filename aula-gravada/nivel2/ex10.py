numero = int(input("Digite um numero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("O{número}é multiplo de 3 e de 5")
elif numero % 3 == 0:
    print("O{número}é multiplo de 3")
elif numero % 5 == 0:
    print("O{númeor} é multiplo de 5")
else:
    print("O{número}não é multiplo de 3 e de 5")