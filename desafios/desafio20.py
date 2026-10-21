print("| DUAS OPÇÕES |")
print("-"*60)

print("Você quer pastel de 'carne' ou pastel de 'queijo'?")
pastel = input("> Digite aqui: ")

if pastel == "carne" or pastel == "queijo":
    print(f"Pronto! Seu pedido de pastel de {pastel} está pronto!")
else:
    print(f"Seu pedido de pastel de pastel de {pastel} não existe")