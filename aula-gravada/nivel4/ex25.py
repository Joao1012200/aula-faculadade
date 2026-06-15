n = int(input("Digite um numero (0 para sair)"))
positivo = 0
negativo = 0

while n != 0:
    if n > 0:
        positivo += 1
    else:
        negativo += 1

    n = int(input("Digite um numero (0 para sair)"))

print(f"Positivo: {positivo}")
print(f"Negativo: {negativo}")