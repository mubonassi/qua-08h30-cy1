print("| ADIÇÃO E SUBTRAÇÃO |")
print("-"*60)

print("| Você deseja realizar 'subtração' ou 'adição?' |")
op = input("> Digite aqui: ")

num1 = int(input("> Digite aqui o #1 número: "))
num2 = int(input("> Digite aqui o #2 número: "))

if op == "adição":
    resultado = num1+num2
    print(f"{num1} + {num2} = {resultado}")
elif op == "subtração":
    resultado = num1-num2
    print(f"{num1} - {num2} = {resultado}")
else:
    print("Opção incorreta!")