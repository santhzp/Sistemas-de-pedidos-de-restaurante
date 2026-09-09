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
elif produto_num == 3:
    print("Você escolheu o Cappuccino")
    print("Preço: R$14")
elif produto_num == 4:
    print("Você escolheu o Latte")
    print("Preço: R$16")  
else:
    print("Opção invalida")

preco = 0

if produto_num == 1:
    preco = 7
elif produto_num == 2:
    preco = 10
elif produto_num == 3:
    preco = 14  
else:
    preco = 16  

quantidade = input("Quantidade: ")
quant_num = int(quantidade)



total = quant_num * preco
print(total)