ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"o {ano} é bissexto")
else:
    print(f"o {ano} não é bissexto")