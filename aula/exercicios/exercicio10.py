dia = int(input("Digite um numero: "))

if dia >= 1 and dia <= 7:
    if dia == 1:
        dia = "Domingo"
    elif dia == 2:
        dia = "Segunda"
    elif dia == 3:
        dia = "Terça"
    elif dia == 4:
        dia = "Quarta"
    elif dia == 5:
        dia = "Quinta"
    elif dia == 6:
        dia = "Sexta"
    elif dia == 7:
        dia = "Sabado"
else:
    dia = 'Dia invalido'
print(dia)
