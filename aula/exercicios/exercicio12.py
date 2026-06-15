hora = float(input("Qual o valor da sua hora?"))
horatrabalhada = float(input("Quantas horas você trabalhou esse mês?"))
fgts = 0.11
sindicato = 0.03

bruto = hora * horatrabalhada

if bruto > 2500.00:
    desconto = bruto - 