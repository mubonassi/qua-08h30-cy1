print("| ENTRANDO NO BAR |")
print("-"*60)

nome = input("> Digite o seu nome: ")
idade = int(input("> Digite a sua idade: "))

if idade >= 18:
    print(f"Seja bem-vindo, {nome}!")
else:
    print(f"Você está barrado, {nome}! Precisa ser maior de idade! DÊ UM FORA!")