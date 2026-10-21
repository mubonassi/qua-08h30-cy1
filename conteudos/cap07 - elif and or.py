#Estrutura de Condição - PT.2
#Estrutura ENCADEADA e COMPOSTA

numero = int(input("> Digite um número: "))

#If Composto (AND e OR) -> Trabalhando com múltiplas condições
#OR (ou) -> Exige que pelo menos UMA condição seja verdadeira
if numero == 4 or numero == 7 or numero == 47:
    print("Você digitou um dos dois números mágicos!")
else:
    print("Você NÃO digitou um dos dois números mágicos!")

#AND (e) -> Exige que TODAS AS CONDIÇÕES sejam verdadeiras
if numero >= 0 and numero <= 10:
    print("Você digitou um número entre 0 e 10")
else:
    print("Você NÃO digitou um número entre 0 e 10")

#If Encadeado -> Trabalhando com múltiplas perguntas/estruturas
#elif -> Uma condição caso a anterior tenha sido negativa
#else if -> senão se
if numero > 0:
    print("O número é positivo!")
elif numero < 0:
    print("O número é negativo!")
else:
    print("O número é neutro!")