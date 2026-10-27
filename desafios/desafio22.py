print("| CALCULADORA DE CONVERSÕES |")
print("-"*60)

print("| Escolha entre: Celsius, Fahrenheit e Kelvin")

grauDigitado = input("> Digite o grau que será digitado: ").strip().capitalize()
temperatura = float(input("> Digite o valor da temperatura: "))
grauConvertido = input("> Digite o grau que será convertido: ").strip().capitalize()

temperaturaConvertida = False

if grauDigitado == "Celsius" and grauConvertido == "Fahrenheit":
    temperaturaConvertida = (temperatura * 1.8) + 32
elif grauDigitado == "Celsius" and grauConvertido == "Kelvin":
    temperaturaConvertida = temperatura + 273.15
elif grauDigitado == "Fahrenheit" and grauConvertido == "Celsius":
    temperaturaConvertida = (temperatura - 32) / 1.8
elif grauDigitado == "Fahrenheit" and grauConvertido == "Kelvin":
    temperaturaConvertida = ((temperatura - 32) / 1.8) + 273.15
elif grauDigitado == "Kelvin" and grauConvertido == "Celsius":
    temperaturaConvertida = temperatura - 273.13
elif grauDigitado == "Kelvin" and grauConvertido == "Fahrenheit":
    temperaturaConvertida = ((temperatura - 273.13) * 1.8) + 32
elif grauDigitado == grauConvertido:
    print("ERRO: Ambas temperaturas com mesmo tipo!")
else:
    print("ERRO: Algum valor deu errado!")

if temperaturaConvertida != False:
    print(f"Valor convertido: {temperaturaConvertida}")