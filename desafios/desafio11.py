print("| Celsius > Fahrenheit/Kelvin |")
print("-"*60)

celsius = float(input("Digite a temperatura em ºC: "))

fahrenheit = (celsius * 1.8) + 32
kelvin = celsius + 273.15

print(f"ºC: {celsius}")
print(f"ºF: {fahrenheit}")
print(f"ºK: {kelvin}")
