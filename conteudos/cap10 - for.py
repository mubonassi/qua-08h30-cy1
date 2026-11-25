#Estruturas de Repetição
#São estruturas/controle de código que permite que um bloco de comandos possa ser repetido por um número de vezes

#FOR -> Repetição contada (quantidade definida) - É determinado quantas X vezes o código será executado

#Para cada número dentro do alcance de 5 numeros

#i -> é uma variável que irá guardar o indice da contagem (index)
#range(x) -> define quantas vezes/ou o intervalo que o código será executado
#[0,1,2,3,4]

for i in range(5):
    print("teste")
print("-- Fim da Repetição --")

#Utilizar a variável da repetição no código
for numero in range(5):
    print(numero)
print("-- Fim da Repetição --")

#Personalizando a nossa repetição
#Determinando qual o indice(numero) irá começar a repetição no range(x)
for i in range(1,6):
    print(i)
print("-- Fim da Repetição --")

#Determinando o passo(step) de cada repetição
for i in range(10,101,10):
    print(i)
print("-- Fim da Repetição --")