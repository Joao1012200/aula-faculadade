def decimal_para_binario(decimal):
    return bin(decimal)[2:]

n = int(input("Digite um numero decimal: "))
if n >= 0:
    print(decimal_para_binario(n))
else:
    print("O numero deve ser positivo")