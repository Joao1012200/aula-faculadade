idade = 0
soma = 0
media = 0

if idade >= 0:
    for i in range (0, 5):
        idade = int(input("Digite a idade: "))
        soma += idade
        media = soma / 5
else:
    print("Idade invalida")

print(f"A média das idades é: {media}")

