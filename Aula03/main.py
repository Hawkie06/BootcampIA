texto1 = '"um texto"'
print(texto1)

texto2 = "'um texto'"
print(texto2)

str1 = "Um"
str2 = " texto"
print(str1 + str2)

val = 5
mystr1 = f"O valor é: {val}"
print(mystr1)

val = 5
mystr2 = f"O número é par? {"Sim" if val % 2 == 0 else "Não"}"
print(mystr2)

mystr3 = "Um texto"
print(mystr3[0])
print(mystr3[0:2])


mystr4 = "Um texto"
print(mystr4.lower())

mystr5 = "Um texto"
print(mystr5.upper())

mystr6 = "Um texto"
print(mystr6.split())

mystr7 = "Um-texto"
print(mystr7.split('-'))

path = "meu_arquivo.txt"
print(path[:-4])
print(path.split('.txt'))
print(path.split('.txt')[0])


print(path.removeprefix('meu'))
print(path.removesuffix('.txt'))
print(path.find('arquivo'))
print(path.replace('meu','nosso'))
print(path.strip())
