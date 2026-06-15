A = int(input("Informe um valor para a variavel A: "))
B = int(input("Informe um valor para a variavel B: "))

if A > B:
    aux=A;
    A=B;
    B=aux;

print("O valor da variavel A agora é :", A)
print("O valor da variavel B agora é :", B)