import time
print("| SORVETERIA PYTHONESCA |")
print("-"*60)

sabores = ["Chocolate","Flocos","Creme","Morango","Abacaxi","Maracuja","Bombom","Trufa"]
coberturas = ["MMs","Chocolate quente","Chocolate branco","Fini","Python.py","Ovomaltine"]
time.sleep(2)
print(">> Lista de sabores")
print(sabores)
print(">> Lista de coberturas")
print(coberturas)
print("-"*60)
print(">>> Escolha o seu sabor")
sabor = input("> Digite aqui: ").capitalize()

if sabor in sabores:
    print(">>> Deseja cobertura? (S ou N)")
    escolha = input("> Digite aqui: ").upper()
    if escolha == "S":
        print(">>> Escolha a sua cobertura")
        cobertura = input("> Digite aqui: ")
        print("!Pedido completo!")
        if cobertura in coberturas:
            print(f"Resumo do pedido: Sorvete de {sabor} com {cobertura}")
        else:
            print("!!!Cobertura não encontrada!!!")
            print(f"Resumo do pedido: Sorvete de {sabor}")
    else:
        print("!Pedido completo!")
        print(f"Resumo do pedido: Sorvete de {sabor}")
else:
    print("!!!Sabor não encontrado!!! Pedido cancelado!")