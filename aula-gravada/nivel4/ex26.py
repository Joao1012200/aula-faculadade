n = int(input("Digite um numero (0 para sair)"))
maior = n


while n != 0:
    if n > maior:
        maior = n

    n = int(input("Digite um numero (0 para sair)"))

print(f"O maior numero é: {maior}")