# Cria uma string usando aspas simples dentro de aspas duplas
texto1 = '"um texto"'
print(texto1)

# Cria uma string usando aspas duplas dentro de aspas simples
texto2 = "'um texto'"
print(texto2)

str1 = "Um"
str2 = " texto"
# Concatena (junta) as duas strings
print(str1 + str2)



val = 5
# f-string permite colocar o valor de uma variável diretamente no texto
mystr1 = f"O valor é: {val}"
print(mystr1)


# Verifica se o valor é par usando o operador %
# Se o resto da divisão por 2 for 0, retorna "Sim"
# Caso contrário, retorna "Não"
mystr2 = f"O número é par? {'Sim' if val % 2 == 0 else 'Não'}"
print(mystr2)



mystr3 = "Um texto"
# Acessa o caractere que está no índice 0
# Em Python, os índices começam em 0
print(mystr3[0])

# Acessa os caracteres do índice 0 até antes do índice 2
# Resultado: "Um"
print(mystr3[0:2])

mystr4 = "Um texto"
# lower() transforma todos os caracteres em letras minúsculas
print(mystr4.lower())

mystr5 = "Um texto"
# upper() transforma todos os caracteres em letras maiúsculas
print(mystr5.upper())

mystr6 = "Um texto"
# split() separa a string usando o espaço como separador
# Resultado: ["Um", "texto"]
print(mystr6.split())

mystr7 = "Um-texto"
# split('-') separa a string sempre que encontrar um hífen
# Resultado: ["Um", "texto"]
print(mystr7.split('-'))


path = "meu_arquivo.txt"
# Remove os últimos 4 caracteres da string
# Como ".txt" possui 4 caracteres, sobra apenas "meu_arquivo"
print(path[:-4])

# Divide a string usando ".txt" como separador
# Resultado: ["meu_arquivo", ""]
print(path.split('.txt'))

# Divide a string e acessa o elemento de índice 0
# Resultado: "meu_arquivo"
print(path.split('.txt')[0])


# Remove o prefixo "meu" do início da string
# Resultado: "_arquivo.txt"
print(path.removeprefix('meu'))

# Remove o sufixo ".txt" do final da string
# Resultado: "meu_arquivo"
print(path.removesuffix('.txt'))


# Procura a posição em que a palavra "arquivo" começa
# Retorna o índice do primeiro caractere encontrado
print(path.find('arquivo'))

# Substitui todas as ocorrências de "meu" por "nosso"
# Resultado: "nosso_arquivo.txt"
print(path.replace('meu', 'nosso'))

# Remove espaços em branco no início e no final da string
print(path.strip())
