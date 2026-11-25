print("| PARES E IMPARES |")
print("-"*60)

valor = int(input("> Digite o valor do intervalo: "))

pares = ""
for i in range(2, valor+1, 2):
    pares = pares + str(i) + " "
print(f"Pares: {pares}")

impares = ""
for i in range(1, valor+1, 2):
    impares = impares + str(i) + " "
print(f"Impares: {impares}")