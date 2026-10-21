print("| RANKING DO JOGO BORKISBOOKI |")
print("-"*60)

pontos = int(input("> Digite a sua pontuação do jogo: "))

if pontos < 0:
    print("ERRO: Valor inválido!")
elif pontos <= 100:
    print("Ranking: Iniciante")
elif pontos <= 250:
    print("Ranking: Treinador")
elif pontos <= 500:
    print("Ranking: Veterano")
elif pontos <= 750:
    print("Ranking: Campeão")
elif pontos <= 1000:
    print("Ranking: Mestre")
else:
    print("Ranking: Lendário")