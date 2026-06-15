carro = "fusca"
ano = 1972
preco = 2500.50

# Interpolação de texto
print("Carro: " + carro + ", Preço: " + str(preco))

# Formas antigas de interpolação
print("Carro: %s, ano: %d, preço: %f" % (carro, ano, preco))

# Versões mais novas
print("Carro: {}, ano: {}, preço: {}".format(carro, ano, preco))
print("Carro: {0}, ano: {1}, preço: {2}".format(carro, ano, preco))

# Versões atuais
print(f"Carro: {carro}, ano: {ano}, preço: {preco}")