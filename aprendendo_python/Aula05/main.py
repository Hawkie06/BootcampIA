#TUPLAS
#Diferente dos dicionários, são imutáveis.

mytuple = (10,) #Necessário a vírgula para entender como tupla

print(type(mytuple))

dados = ("Náthally", 10, True) #Diferentes tipos como os dicionário e listas, pode ter listas e dicionários dentro dela.

dados = ("Náthally", [8.5,7.0,9.0]) #As tuplas são imutáveis, porém se os elementos são mutáveis, eles são alteráveis.

dados [1][0] = 10.0

print(dados)

numeros = (0, 1, 2, 3, 4, 5) #Slice igual em listas e dicionários

print(numeros[1:4])
print(numeros[::-1])

nomes = ("Gabriel", "Maria", "João") #Podem ser percorridas com for 

for nome in nomes:
    print(nome)