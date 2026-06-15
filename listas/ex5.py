def contagem(n):
    if n == 0:
        print("Lançar!!!")
        return

    print(n)
    contagem(n - 1)

# programa principal
contagem(5)