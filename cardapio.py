print("--------------------")

print("     CARDÁPIO       ")

print("--------------------\n")

print("BEBIDAS QUENTES:\n")

print("1 - Expresso único (Forte, Marcante e Intenso) - R$7 ")
print("2 - Expresso duplo (Dose dupla) - R$10 ")
print("3 - Cappuccino (Mistura única de leite, café e chocolate) - R$14 ")
print("4 - Latte (Uma dose de expresso único com delicioso leite vaporizado) - R$16 ")

add_produto = "S"
total = 0

while add_produto == "S":

    produto = input("Escolha o produto: ")
    produto_num = int(produto)

    while produto_num not in (1, 2, 3, 4):
        print("Opção inválida, tente novamente.")
        novo_produto = input("Escolha o produto: ")
        produto_num = int(novo_produto)

    if produto_num == 1:
        preco = 7
        print("Você escolheu o Expresso único")
        print("Preço: R$7 ")

    elif produto_num == 2:
        preco = 10
        print("Você escolheu o Expresso Duplo")
        print("Preço: R$10 ")

    elif produto_num == 3:
        preco = 14
        print("Você escolheu o Cappuccino")
        print("Preço: R$14")

    elif produto_num == 4:
        preco = 16
        print("Você escolheu o Latte")
        print("Preço: R$16")

    quantidade = input("Quantidade: ")
    quant_num = int(quantidade)

    compra_atual = quant_num * preco


    add_produto = input("Deseja adicionar outro produto? [S/N]\n").upper()

    total = total + compra_atual

    print("Total: R${:.2f}".format(total))