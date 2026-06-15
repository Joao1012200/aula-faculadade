user = str(input("Digite seu usuario: "))
password = str(input("Digite sua senha: "))

while user == password:
    print("login invalido, por favor tente novamente")
    user = str(input("Digite seu usuario: "))
    password = str(input("Digite sua senha: "))
else:
    print("login feito com sucesso")