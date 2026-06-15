def eh_palindromo(palavra):
    palavra = palavra.lower()
    return palavra == palavra[::-1]


palavra = input("Informe uma palavra: ")
if eh_palindromo(palavra):
    print("Palindromo")
else:
    print("Não é palindromo")