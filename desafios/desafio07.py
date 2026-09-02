print("| CALCULO DE TEMPO DE VIAGEM |")
print("-"*60)

velocidade = float(input("Digite a sua velocidade (km/h): "))
distancia = float(input("Digite a distancia (km): "))

tempo = distancia/velocidade

print(f"Tempo de viagem: {tempo}hrs")