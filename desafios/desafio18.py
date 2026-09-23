print("| ENCHENDO UMA PISCINA |")
print("-"*60)

capacidade = int(input("> Digite a capacidade (em L) da piscina: "))
falta = int(input("> Digite o quanto está faltando (em L): "))

if falta <= capacidade:
    encher = int(input("> Digite o quanto será enchido (em L): "))
    if encher <= falta:
        total = capacidade - falta + encher
        print("Piscina enchida com sucesso!")
        print(f"Total atual: {total}L")
    else:
        print("!! Piscina transbordou !!")
else:
    print("!! Valor Inválido !!")