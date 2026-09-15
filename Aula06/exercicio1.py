val = input().split()
operacao = input()
val_ = []
for i in val:
    val_.append(int(i))




def operacoes(numeros, op = "soma"):
    resultado = val_[0]

    if op not in ["soma", "subtração", "multiplicação", "Divisão"]:
        op = "soma"

    if op == "soma":
        for i in numeros[1:]:
            resultado = resultado + i
        return resultado
    elif op == "divisão":
        for i in numeros[1:]:
            if i == 0:
                
            else:
                
        return resultado        
    elif op == "subtração":
        for i in numeros[1:]:
            resultado = resultado - i
        return resultado    
    elif op == "multiplicação":
        for i in numeros[1:]:
            resultado = resultado * i
        return resultado


print(operacoes(val_,operacao))
