print("| LOLJA |")
print("-"*60)

produtos = ["Doritos","Doritos do League of Legends","Martelo","Prego do LOL","Coxinha RGB"]

print("| Lista de Produtos |")
print(produtos)
print("-"*60)

print(">> Escolha o seu produto!")
escolha = input("Digite aqui: ").strip()

if escolha in produtos:
    print(f"Você escolheu {escolha}! Boa escolha!")
else:
    print("que isso")