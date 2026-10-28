print("| RESTAURANTE PYTHONICO |")
print("-"*60)

cardapio = ["Arroz com Feijão","Sorvete","Feijoada","Coxinha","Purê de Python","Baguete","Chocolate Quente","Cadeira de Sorvete","Sei lá","Pizza Doce Salgada","Pizza Salgada Doce","Sim"]

print("| Cardápio |")
print(cardapio)
print("-"*60)

escolha = int(input(">> Digite qual o prato desejado (pelo indice): "))

if escolha >= 0 and escolha < len(cardapio):
    print(f">> Você escolheu {cardapio[escolha]}")
else:
    print("Desculpa! Esse prato não existe")