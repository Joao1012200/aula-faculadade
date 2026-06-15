def numero_usuario(n):
    if n >= 0 and n <= 10:
        return print("O numero esta entre 0 e 10")
    else:
        return print("O numero nao esta entre 0 e 10")

n = int(input("Informe um numero:"))
print(numero_usuario(n))
