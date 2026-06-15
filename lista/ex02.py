distancia = int(input("Informe a distância percorrida em km: "))
gas = int(input("Informe a quantidade de combustível gasto: "))

media = distancia / gas

print("O consumo médio foi de, %.2f " % media, "km, por litro")