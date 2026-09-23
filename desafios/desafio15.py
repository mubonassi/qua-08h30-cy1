print("| VERIFICADOR DE MÉDIA |")
print("-"*60)

nota1 = float(input("> Digite a #1 Nota: "))
nota2 = float(input("> Digite a #2 Nota: "))
nota3 = float(input("> Digite a #3 Nota: "))
minima = float(input("> Digite a nota de corte (média mínima): "))

media = (nota1+nota2+nota3)/3

print(f"Média Final: {media}")

if media >= minima:
    print("Você foi aprovado")
else:
    print("Você foi REPROVADO!")