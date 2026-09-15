print("| CARRINHO DE COMPRAS |")
print("-"*60)

produto1 = input("> Digite o nome do produto (1): ")
valor1 = float(input("> Digite o valor do produto (1): "))
produto2 = input("> Digite o nome do produto (2): ")
valor2 = float(input("> Digite o valor do produto (2): "))
produto3 = input("> Digite o nome do produto (3): ")
valor3 = float(input("> Digite o valor do produto (3): "))

total = valor1 + valor2 + valor3
credito = total * 1.05
vista = total * 0.985

print("| Carrinho |")
print(f"| {produto1} | R${valor1} |")
print(f"| {produto2} | R${valor2} |")
print(f"| {produto3} | R${valor3} |")
print("| Total |")
print(f"> R${total}")
print("| Formas de Pagamento |")
print(f"> Débito: R${total}")
print(f"> Crédito: R${credito}")
print(f"> À Vista (dinheiro): R${vista}")