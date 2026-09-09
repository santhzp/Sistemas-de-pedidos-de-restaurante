print("--------------------")
print("     CARDÁPIO       ")
print("--------------------\n")

print("BEBIDAS QUENTES:\n")

print("1 - Expresso único (Forte, Marcante e Intenso) - R$7 ")
print("2 - Expresso duplo (Dose dupla) - R$10 ")
print("3 - Cappuccino (Mistura única de leite, café e chocolate) - R$14 ")
print("4 - Latte (Uma dose de expresso único com delicioso leite vaporizado) - R$16 ")

produto = input("Escolha o produto: ")

produto_num = int(produto)

if produto_num == 1: 
    print("Você escolheu o Expresso único")
    print("Preço: R$7 ")
elif produto_num == 2:
    print("Você escolheu o Expresso Duplo")
    print("Preço: R$10 ")


