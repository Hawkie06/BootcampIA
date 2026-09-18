import pandas as pd

#Carregando dados
data = pd.read_csv('./dados.csv')

#Printando os tipos das colunas
print(data.dtypes)

#Printando infos das colunas
print(data.info())

#Remover coluna da base de dados
data = data.drop(columns=["Carimbo de data/hora"])

print(data.info())

#Seleciona a coluna deseja e realiza a contagem de valores únicos
vu = data["Idade"].value_counts()
print(vu)

#Transformando os dados da coluna idade
data["Idade"] = data["Idade"].replace({"19 anos": "19"})
vu = data["Idade"].value_counts()
print(vu)

#Mudar tipo de dado
data["Idade"] = data["Idade"].astype(int)
print(data.info())

