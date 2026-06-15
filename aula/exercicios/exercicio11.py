salario = float(input("Informe o sálario: "))

if salario <= 280.00:
    reajuste = 0.20
    valor = salario * reajuste
    novo = salario + valor
elif salario > 280.00 and salario <= 700.00:
    reajuste = 0.15
    valor = salario * reajuste
    novo = salario + valor
elif salario > 700.00 and salario <= 1500.00:
    reajuste = 0.05
    valor = salario * reajuste
    novo = salario + valor
else:
    print("Você não recebe aumento")
print("O sálario era:" , salario,
    "\nO percentual foi de: ", reajuste,
    "\nO valor do aumento foi de: %.2f" % valor,
    "\nO novo salario é: %.2f" % novo)