# Tipos de variáveis
varb = 1
varc = "abcd"
vard = 0.123
varf = True #False


# Operações com inteiro 

op1 = 1 + 3
op2 = 1 - 3
op3 = 1 * 3
op4 = 1 / 3
op5 = 1//3 # Divisão que resulta em int
op6 = 2 ** 2 # Potenciação
op6 = 3%5 # Módulo

# Operadores Lógicos
print(3 == 3) # Igualdade
print(3 != 2) # Desigualdade
print (5 > 3) # Maior
print (5 < 8) # Menor
print (5 <= 8) # Menor igual
print (5 >= 3) # Maior igual

var1 = 3
var2 = var1
print(var1 is var2) # Idêntico: verifica se é o mesmo valor(imutável), não a referência. 
print(not var1 is var2) # Não Idêntico

print(3 == 2 or 1 == 1)
print(3 == 2 and 1 == 1)
print(not 2==2 or 3 == 2 and 1 == 1) # Not sempre o último a ser executado, and primeiro.

# Operações com String

print ("abcd" == "abcd")
print ("abcd" != "abcde")
print ("abcde" > "abcd")
print ("abc" < "abcd")
print ("abcd" >= "abcd")
print ("abcd" <= "abcd")

# Condicionais

if 3 > 2:
    print ("Condição")
elif 2 == 2:
    print ("elif")    
else: 
    print("Condiçaõ falsa")    

varmatch = 3

match varmatch:
    case 1:
        print("Valor 1")
    case 2:
        print("Valor 2")        
    case 3:
        print("Valor 3") 
    case _:
        print("default!")                

# print(type()) -> mostra o tipo
# print(id()) -> mostra o ID 