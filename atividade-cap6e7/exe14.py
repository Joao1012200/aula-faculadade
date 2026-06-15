"""
    Faça um programa que lê o valor em reais e calcule o valor
    equivalente em dólares. O usuário deve informar , além do valor
    em reais da compra, o valor da cotação do dólar.
"""
reais = float(input("Digite o valor em reais: "))
cotacao = float(input("Digite o valor da cotação do dólar: "))

total = reais/cotacao
print("Você possui",total," em dólares")
