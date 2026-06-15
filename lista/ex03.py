cod = int(input("Digite o codigo: "))
salario = float(input("Digite o salario: "))
vendas = float(input("Digite o valor de vendas: "))

comissao = vendas * 0.15
ganho = salario + comissao

print("O total ganho em comissão foi de: %.2f" % comissao,
      "\nO total que esse vendedor ganhou foi de: %.2f" % ganho)