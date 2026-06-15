qtd = 0
soma = 0
media = 0

while True:
    valor = float(input("Digite a nota: "))
    if valor < 0: break
    soma = soma + valor
    qtd += 1

media = soma / qtd
print(f"Média: {media:.2f}")