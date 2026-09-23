print("| POSITIVO, NEGATIVO OU NEUTRO |")
print("-"*60)

valor = float(input("> Digite um valor: "))

if valor > 0:
    print("O valor é positivo!")
else:
    if valor < 0:
        print("O valor é negativo!")
    else:
        print("O valor é neutro (zero)!")