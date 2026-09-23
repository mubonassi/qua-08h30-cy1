print("| POSTO DE PYTHONLINA |")
print("-"*60)

abastecido = float(input("> Digite a quantidade (L) que será abastecido: "))
litro = float(input("> Digite o valor do litro: R$"))

total = abastecido * litro

print(f"| Total: R${total} |")
pagamento = float(input("> Digite o quanto será pago: "))

if pagamento >= total:
    print("Pagamento realizado com sucesso!")
    if pagamento > total:
        troco = pagamento - total
        print(f"Troco: R${troco}")
else:
    print("Valor insuficiente para pagamento")