print("| VERIFICAÇÃO DE CONVITE |")
print("-"*60)

idade = int(input("> Digite a sua idade: "))
convite = input("> Você tem convite? (S ou N): ")

if idade >= 18 and convite == "S":
    print("Você poderá entrar! Seja bem vindo!")
elif idade <= 18 and convite == "N":
    print("NENHUM DOS DOIS? VAZA!")
elif idade < 18:
    print("Você é menor de idade! Não poderá entrar!")
elif convite == "N":
    print("Você não foi convidado! Vaza!")
else:
    print("...que?")