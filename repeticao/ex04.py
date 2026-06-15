print("digite sair no nome para encerar")
while True:
    nome = str(input("Digite seu nome completo: "))
    if nome == "sair":
        print("Encerando...")
        break
    while len(nome) <= 3:
        print("O nome deve conter mais de 3 caracteres")
        nome = str(input("Digite seu nome completo: "))

    idade = int(input("Digite sua idade: "))
    while idade < 0 or idade > 150:
        idade = int(input("Digite uma idade valida: "))

    salario = float(input("Digite seu salario: "))
    while salario < 0:
        salario = float(input("Digite um salario valido: "))

    estado_civil = str(input("Digite seu estado civil: [S/C/V/D]")).upper()
    while estado_civil not in ["S", "C", "V", "D"]:
        estado_civil = str(input("Digite seu estado civil: [S/C/V/D]")).upper()