#Formatando String
#São funções que podem ou alterar o valor da string ou alterar a exibição do valor

print("| Formatando String |")

frase = "      Banana com maçã e Café       "

print(frase)
print(frase.upper()) #Upper -> Tudo maiusculo
print(frase.lower()) #Lower -> Tudo minusculo
print(frase.title()) #Title -> Coloca a primeira letra de palavra maiuscula
print(frase.capitalize()) #Capitalize -> Apenas a primeira letra maiuscula
print(frase.strip()) #Strip -> Remove os espaços no inicio e no fim
print(frase.swapcase()) #Swapcase -> Inverte o maiusculo com minusculo
print(frase.replace("Banana","Abacaxi")) #Replace -> Substitui uma palavra na string por outra