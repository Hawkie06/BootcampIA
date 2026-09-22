import pandas as pd

#Carregando dados
data = pd.read_csv('./dados.csv')

# #Printando os tipos das colunas
# print(data.dtypes)

# #Printando infos das colunas
# #print(data.info())

# #Remover coluna da base de dados
data = data.drop(columns=["Carimbo de data/hora"])

# #Seleciona a coluna deseja e realiza a contagem de valores únicos
# vu = data["Idade"].value_counts()
# #print(vu)

# #Transformando os dados da coluna idade
data["Idade"] = data["Idade"].replace({"19 anos": "19"})
vu = data["Idade"].value_counts()
#print(vu)

# #Mudar tipo de dado
data["Idade"] = data["Idade"].astype(int)
# print(data.info())

# print(data["Altura"].value_counts())

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
# print(vt)

# print(data.info())

# print(data["Semestre/Período"].value_counts)

def filtro_semestre(texto: str):
    texto = texto.lower().replace("semestre", "").replace("bimestre", "").strip()
    texto = texto.replace("segundo", "2").replace("sexto","6")
    return int(texto[0])

vt = data["Semestre/Período"].apply(filtro_semestre)
# print(vt.value_counts())


data = data.rename(columns={"Semestre/Período": "periodo"})
data["periodo"] = vt
# print(data.info())


#print(data["Faz atividade física? (crossfit, academia, artes marciais)"].value_counts())
collumn_name = "Faz atividade física? (crossfit, academia, artes marciais)"
data[collumn_name] = data[collumn_name].replace({"Sim": True, "Não": False})
data = data.rename(columns={collumn_name: "ativi_fisi"})
# print(data["ativi_fisi"].value_counts())
# print(data.info())


# #Variáveis categóricas

# print(data["Curso"].value_counts())

def transformacao_curso(texto: str):
    texto = texto.lower()
    if "dado" in texto:
        texto = "ciencia de dados"
    elif "software" in texto:
        texto = "engenharia de software"
    elif "informa" in texto or "s.i" in texto:
        texto = "sistemas de informação"
    elif "computação" in texto:
        texto = "ciência da computação"
    elif "desenv" in texto or "ads" in texto:
        texto = "ads"               
    # texto = texto.replace("&", "e").replace("ç","c").replace("á","a")
    # texto = texto.replace("á","a").replace("é", "e").replace("ê","e")


    return texto

vt = data["Curso"].apply(transformacao_curso)
# print(vt.value_counts())

data = data.drop(columns=["Cidade natal"])
data = data.drop(columns=["Turno"])
# print(data.info())

def transformacao_instituicao(text:str):
    text = text.lower().strip()
    if "unifil" in text:
        text = "uniil"
    elif "utfpr" in text:
        text = "utfpr"
    
    return text    

vt = data["Instituição de ensino"].apply(transformacao_instituicao)
#print(vt.value_counts())
data = data.rename(columns={"Instituição de ensino": "universidade"})
data["universidade"] = vt

# print(data.info())

def transformacao_linguagem(text: str):
    text = text.strip().lower().split(",")[0].split()[0]   
    return text       

collumn_name1 = "Linguagem de programação com experiência" 
vt = data[collumn_name1].apply(transformacao_linguagem)
# print(vt.value_counts())
data = data.rename(columns={collumn_name1: "lang"})
data["lang"] = vt

# print(data.info())

def transformacao_comfav(text:str):
    text = text.lower().strip()
    if "hamb" in text or "lanche" in text:
        text = "lanche"

    elif "jap" in text:
        text = "japonesa"

    elif "chur" in text:
        text = text
    elif not("." in text or "strog" in text or "comi" in text or "fric" in text):
        text = "massa"
    else:
        text = "outros"    
    return text


collumn_name2 = "Comida favorita (Hamburger, pizza, japonesa, alemã)"
vt = data[collumn_name2].apply(transformacao_comfav)
# print(vt.value_counts())
data = data.rename(columns={collumn_name2: "comida_fav"})
data["comida_fav"] = vt
# print(data.info())

def transformacao_hobby(text: str):
    text = text.lower()
    if "," in text:
        text = text.split(",")[0]

    esportes = ["fut","bola","vôlei","espor", "pipa", "patins"]
    for esporte in esportes:
        if esporte in text:
            text = "esporte"
            break

    jogos = ["jog", "valora", "fifa", "rpg", "tcg", "game", "level"]
    for jogo in jogos:
        if jogo in text:
            text = "jogos"
            break     

    artes = ["ler", "desen", "edição", "vocalista", "bateria", "aula"]     
    for arte in artes:
            if arte in text:
                text = "artes"
                break   

    if not text in ["esporte","jogos", "artes"]:
        text = "outros"
        
    return text       

vt  = data["Hobby"].apply(transformacao_hobby)
# print(vt.value_counts())

def transformacao_area(text: str):
    text = text.lower()


    areas_ia = ["a.i", "cien", "dado", "data", "artific", "machi", "gener", "ia"]
    for area in areas_ia:
            if area in text:
                text = "ciencia_dados/ia"
                break

    areas_dev = ["desenv", "dev", "front", "back"]
    for area in areas_dev:
            if area in text:
                text = "dev"
                break

    areas_gest = ["gest", "product", "agile", "ceo", "proje"]
    for area in areas_gest:
            if area in text:
                text = "gestao/diretoria"
                break

    if not text in ["ciencia_dados/ia", "gestao/diretoria", "dev"]:
        text = "n/d"

    return text

column_name = "Área de atuação desejada"
data = data.rename(columns={column_name: "area_atuacao"})
vt = data["area_atuacao"].apply(transformacao_area)
# print(vt.value_counts())
data["area_atuacao"] = vt
# print(data.info())

subs = {
    "Bring me the Horizon": "rock",
    "Naldo Benny": "pop",
    "Don L": "rap",
    "Zendaya": "pop",
    "Slipknot, Korn, System, Drowingpool, Jorge Matheus": "rock",
    "DJ Ramon Sucesso": "eletronica",
    "Joji": "pop",
    "Harry Style": "pop",
    "Michael Jackson": "pop",
    "Frank sinatra": "pop",
    "Jotape": "rap",
    "Stray Kids e aespa": "pop",
    "Skillet": "rock",
    "Team Impala": "rock",
    "Hungria": "rap",
    "The neighbourhood": "rock",
    "Skank": "rock",
    "System of a Down": "rock",
    "DJ wagner": "eletronica",
    "$uicedeBoy$": "rap",
    "2Zdinizz": "rap",
    "Queen": "rock",
    "Yunk Vino": "rap",
    "Dream Theater": "rock"
}

def transformacao_artista(text: str):
    text = text.lower()
    return text

new_dict = {}
for key in subs:
    new_dict[key.lower()] = subs[key]

data = data.rename(columns={"Artista/Banda favorita": "art_banda","Filme/Anime/Série favorita": "serie"})
vt = data["art_banda"].apply(transformacao_artista)
vt = vt.replace(new_dict)
# print(vt.value_counts())
print(data.info())