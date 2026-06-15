def somatorio_recursivo(numero):
    if numero == 1:
        return 1
    else:
        return numero + somatorio_recursivo(numero - 1)

numero = int(input("digite um numero:"))

if numero > 0:
    result = somatorio_recursivo(numero)
    print(somatorio_recursivo(numero))
else:
    print("insira um numero positivo")