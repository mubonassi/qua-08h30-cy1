print("| JO KEN PO |")
print("-"*60)

print("| Deve-se escolher: pedra, papel ou tesoura |")
print(">> Jogador 1")
jogador1 = input("> Digite seu ataque: ").lower()
print(">> Jogador 2")
jogador2 = input("> Digite seu ataque: ").lower()

vencedor = 0

if jogador1 == jogador2:
    vencedor = 3
elif jogador1 == "pedra" and jogador2 == "papel":
    vencedor = 2
elif jogador1 == "pedra" and jogador2 == "tesoura":
    vencedor = 1
elif jogador1 == "tesoura" and jogador2 == "pedra":
    vencedor = 2
elif jogador1 == "tesoura" and jogador2 == "papel":
    vencedor = 1
elif jogador1 == "papel" and jogador2 == "tesoura":
    vencedor = 2
elif jogador1 == "papel" and jogador2 == "pedra":
    vencedor = 1
else:
    print("*** ERRO: Digite uma opção válida ***")

if vencedor == 3:
    print(">> EMPATE <<")
elif vencedor == 1:
    print(">> JOGADOR 1 VENCEU <<")
    print(f"{jogador1} vence de {jogador2}")
elif vencedor == 2:
    print(">> JOGADOR 2 VENCEU <<")
    print(f"{jogador2} vence de {jogador1}")