import pandas as pd

#Carregando dados
data = pd.read_csv('./dados.csv')

#Printando os tipos das colunas
print(data.dtypes)

#Printando infos das colunas
#print(data.info())

#Remover coluna da base de dados
data = data.drop(columns=["Carimbo de data/hora"])

#Seleciona a coluna deseja e realiza a contagem de valores únicos
vu = data["Idade"].value_counts()
#print(vu)

#Transformando os dados da coluna idade
data["Idade"] = data["Idade"].replace({"19 anos": "19"})
vu = data["Idade"].value_counts()
#print(vu)

#Mudar tipo de dado
data["Idade"] = data["Idade"].astype(int)
print(data.info())

print(data["Altura"].value_counts())

def filtro_altura(texto:str):
    if not texto.isdigit():
        texto = texto.lower()
        texto = texto.replace(".", "").replace(",","").replace("m", "").replace("c","")
        texto = texto.strip()
        if len(texto) == 2:
            texto = f"{texto}0"

        texto = texto[:3]
    return int(texto)

data["Altura"] = data["Altura"].apply(filtro_altura)
vt = data["Altura"].value_counts()
print(vt)

print(data.info())

print(data["Semestre/Período"].value_counts)

def filtro_semestre(texto: str):
    texto = texto.lower().replace("semestre", "").replace("bimestre", "").strip()
    texto = texto.replace("segundo", "2").replace("sexto","6")
    return int(texto[0])

vt = data["Semestre/Período"].apply(filtro_semestre)
print(vt.value_counts())