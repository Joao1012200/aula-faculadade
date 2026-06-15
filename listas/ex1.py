estoque = {
    "maça": 1.50,
    "banana": 0.75,
    "laranja": 2.00,
    "uva": 3.50,
}

carrinho = []


def exibir_cardapio(estoque):
    print("\n==== PRODUTOS DISPONÍVEIS ====")

    for fruta, preco in estoque.items():
        print(f" {fruta}: R${preco:.2f}")
    print("=======================")


# ADICIONAR
def adicionar_item(carrinho, estoque, fruta):
    print("==== ADICIONAR ITEM ====")
    if fruta not in estoque:
        print("A fruta desejada não tem em estoque.")
        return

    carrinho.append(fruta)
    print(f"A {fruta} foi adicionado ao carrinho.")
    print(f"O carrinho agora tem {len(carrinho)} item(s).")

def exibir_carrinho(carrinho, estoque):
    if len(carrinho) == 0:
        print("O carrinho está vazio")
    else:
        for item in carrinho:
            print(f" - {item}: R${estoque[item]:.2f}")

    total = 0
    for item in carrinho:
        total += estoque[item]

    print(f"\nTotal: R$ {total:.2f}")


print("Bem vindo ao sistema de compras da turma de aP 2026.1.")

while True:
    print("\nO que deseja fazer?")
    print(" 1 - Ver produtos disponíveis.")
    print(" 2 - Adicionar item ao carrinho.")
    print(" 3 - Exibir itens e valor total do carrinho.")
    print(" 5 - Finalizar.")

    opcao = input("\nEscolha sua opção: ")

    if opcao == "1":
        exibir_cardapio(estoque)
    elif opcao == "2":
        fruta = input("Qual fruta você deseja adicionar? ").lower()
        adicionar_item(carrinho, estoque, fruta)
    elif opcao == "3":
        exibir_carrinho(carrinho, estoque)
    elif opcao == "5":
        break
    else:
        print("\nOpção inválida. Digite um número de 1 a 5.")