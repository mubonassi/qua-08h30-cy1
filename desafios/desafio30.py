print("| TABUADA CLÁSSICA |")
print("-"*60)

tabuada = int(input("> Digite o valor que será criado a tabuada: "))

for i in range(1,11):
    conta = tabuada * i
    print(f"{tabuada} x {i} = {conta}")