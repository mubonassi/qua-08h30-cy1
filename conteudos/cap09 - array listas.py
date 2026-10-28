#Array/Listas

#Criando uma lista de string
lista = ["A","B","C","D","E","F","G","H"]
print(lista)

#Lista de numeros
listaN = [10,20,30,40]
print(listaN)

#Lista mista  
listaM = [10,"A","B",True,19.99,lista]
print(listaM)

#Exibindo um item especifico
#lista[indice]
#indice é o numero indicador da posição do item na lista
print(lista[1])

#Pegando o número de items
numItems = len(lista)
print(f"Número de itens na lista: {numItems}")

#Verificando um item na lista
item = "D"
if item in lista:
    print(f"O item {item} está dentro da lista!")

item = "J"
if item not in lista:
    print(f"O item {item} NÃO está dentro na lista!")