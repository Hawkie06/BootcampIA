#Estruturas condicionais
n1 = 12

#elif escolhe o primeiro resultado verdadeiro, não printa os outros.
if (n1%2) == 0:
    print("O número é divisível por 2")
elif (n1%3) == 0:
    print("O número é divisível por 3")
elif (n1%4) == 0:
    print("O número é divisível por 4")
else:
    print("O número não é divisível por nenhum dos números acima.")

