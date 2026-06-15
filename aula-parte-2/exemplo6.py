def par_ou_impar(n):
    if n % 2 == 0:
        return print(f"{n} é par")
    else:
        return print(f"{n} é impar")

n = int(input("Informe um numero: "))
print(par_ou_impar(n))