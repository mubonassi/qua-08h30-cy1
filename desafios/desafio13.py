print("| PALAVRA MÁGICA |")
print("-"*60)

palavra = "palavra"
tentativa = input("> Digite a tentativa de palavra mágica: ")

if palavra == tentativa:
    print("VOCÊ ACERTOU!!!!!!!!!!!!!!!!!")
else:
    print("VOCÊ ERROU!!!!!!!!!!!!!!!!!!!")
    print(f"A palavra era {palavra}")