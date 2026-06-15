#lista_numeros = [1, 2, 3, 4, 5]
#print(lista_numeros) nao fazer isso!

lista_palavras = ["casa", "carro", "casa", "trabalho", "casa"]
palavra_antiga = "casa"
palavra_nova = "apartamento"
lista_atualizadas = [palavra_nova if palavra == palavra_antiga else palavra for palavra in lista_palavras]
print(lista_atualizadas)