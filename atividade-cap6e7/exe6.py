frase = "meu nome é Fabrício"

print("nome" in frase)
print("fabricio" in frase)
print("Fabrício" not in frase)

print( len(frase)) # retorna o tamanho da frase

print(frase.lower()) # trabalhando minusculo - não altera a frase original
print(frase.upper())

print(frase) # a frase continua a mesma

print( dir(str)) # dir e suas funções
print( frase.capitalize()) #capitalizar a primeira letra

print( frase.split()) #quebra a frase e cria uma lista

dados = "Fabrício;30anos;1,85;03/07/1991"
print(dados.split(";"))