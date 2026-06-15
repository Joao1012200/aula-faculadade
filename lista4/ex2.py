idade = 0
media = 0
soma = 0

for i in range(1, 6):
    idade = int(input("Digite a idade: "))
    soma += idade
    media = soma / 5

print(f"A media das idades é {media}")