#LISTAS

lista = ["olá", 130]

#lista_exemplo = ["oi", 3, True]
# lista_exemplo.append(0.356)
#lista_exemplo.append(lista)
#lista_exemplo.extend(lista)
#print(lista_exemplo.index("oi"))
#lista_exemplo.insert(1, False)

lista_exemplo = [1,2,3,4,5,6,7,8,9,10]


#print(lista_exemplo[1::2]) -> Índice_de_começo:Índice_de_parada: de_quantos_em quantos_índices_você_vai_avançar
slice1 = lista_exemplo[2:] #Sem o índice de parada, vai até o final da lista
slice2 = lista_exemplo[2:8] #Funciona de forma semelhante ao for: começa no índice 2 e vai até antes do índice 8.
slice3 = lista_exemplo[2:8:3] #Funciona de forma semelhante ao for: começa no índice 2, vai até antes do índice 8 e avança de 3 em 3.
slice4 = lista_exemplo[-1]  #Pega o último índice.
slice5 = lista_exemplo[::-1] #Decrescente
slice6 = lista_exemplo[-4:-10:-1]

# print(len(slice6)) -> Tamanho da lista
# print(lista_exemplo.count(3)) -> Quantas vezes o número aparece na lista

lista_ex = lista_exemplo.copy() #Cria uma cópia preservando o valor da lista original
lista_ex [0] = -1
print(lista_exemplo)
print(lista_ex)

#Extra: deepcopy cria uma nova referência para um novo objeto, copiando também os objetos internos, tornando a cópia independente da original.
#copy cria uma nova referência para o objeto externo, mas mantém referências aos objetos internos.
# O Garbage Collector remove da memória objetos que não possuem mais
# nenhuma referência acessível no programa.
# Apagar uma referência não apaga necessariamente o objeto:
# se ainda existir outra referência para ele, o objeto continua existindo.
# Quando não houver mais nenhuma referência acessível, o objeto fica
# elegível para ser removido pelo Garbage Collector.

#LAÇOS DE REPETIÇÃO

l1 = [1,2,3,4,5,6,7,8,9]

# i = 0
# while i<3: 
#     print(l1[i])
#     i +=1

# for i in l1:
#     print(i)

# for i in l1:
#     print(i)
#     if i == 8:
#         break

for idx in range (8,10):
    print(idx)

arr = [5,6,2,8,1] 
arr.sort()
print(arr)

arr1 = ["Pedro","Ana","Julia"] 
arr1.sort()
print(arr1)