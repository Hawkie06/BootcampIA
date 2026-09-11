#DICIONÁRIO

aluno = {"nome": "João", "nota": 10}

aluno["nome"] = "Pedro"
aluno["nota"] = 10.4

print(aluno["nome"])
print(aluno["nota"])

aluno = {"nome": "Pedro" , "notas": [8 , 9 , 10]}
print(aluno["notas"][1])

aluno = {"nome": "Pedro", "notas": {"geo": 10, "mat": 9, "lp": 8}}
print(aluno["notas"]["mat"])

aluno = {"nome": "Pedro", "notas": {"geo": 10, "mat": 9, "lp": 8}, "apro": True}

print(aluno)
del aluno ["notas"]["geo"]

print(aluno)

aluno = {"nome": "Pedro", "notas": {"geo": 10, "mat": 9, "lp": 8}}

aluno["aprov"] = True
print(aluno)

aluno = {"nome": "Pedro", "notas": [8, 9, 10]}

aluno["notas"][1] = 7
print(aluno)