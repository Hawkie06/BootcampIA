# FUNÇÕES
# Uma função é um bloco de código criado para realizar uma determinada tarefa.
# Ela só é executada quando é chamada.

def saudade():
    print("Olá")

# Chamando a função.
saudade()


# Uma função também pode RETORNAR um valor usando return.
def soma0():
    return 10 + 20

# A função retorna 30, que depois é enviado para o print.
print(soma0())


# A função pode receber uma condição e retornar um valor.
def myfunc(a):
    if a:
        return 10

# Como estamos passando True, a condição é verdadeira
# e a função retorna 10.
print(myfunc(True))


# PARÂMETROS
# Parâmetro é uma informação que a função recebe para poder trabalhar.

def saudacao(nome):
    print(f"Olá, {nome}!")

# "Davi" é o argumento que será colocado no parâmetro "nome".
saudacao("Davi")


# A função pode receber mais de um parâmetro.
def soma1(a, b):
    return a + b

print(soma1(10, 20))


# Podemos fazer validações dentro da função.
def soma2(a, b):

    # Verifica se os dois valores são inteiros.
    if type(a) == int and type(b) == int:
        return a + b

    # Se a condição não for verdadeira, retorna 0.
    return 0

# "Maria" não é int, então a condição é falsa e retorna 0.
print(soma2("Maria", 20))


# PARÂMETROS POSICIONAIS
# Quando passamos os argumentos normalmente, a posição deles
# determina para qual parâmetro cada valor será enviado.

def apresentar(nome, idade):
    print(f"Nome: {nome}")
    print(f"idade: {idade}")

apresentar("João", 20)
# "João" -> nome
# 20      -> idade

apresentar(10, "Julia")
# 10      -> nome
# "Julia" -> idade
#
# Python não impede essa troca porque os dois valores são aceitos.
# O resultado, porém, ficará logicamente errado.


# PARÂMETROS NOMEADOS (KEYWORD ARGUMENTS)
# Podemos informar explicitamente o nome de cada parâmetro.
# Dessa forma, a ordem pode ser alterada.

def apresentar1(nome, idade):
    print(f"Nome: {nome}")
    print(f"idade: {idade}")

apresentar1(idade=20, nome="João")
apresentar1(nome="Julia", idade=10)

# Como usamos "nome=" e "idade=", Python sabe exatamente
# qual valor pertence a cada parâmetro.


# Podemos misturar parâmetros posicionais e nomeados.
def apresentar2(nome, idade, carteira):
    print(f"Nome: {nome}")
    print(f"idade: {idade}")
    print(f"Tem carteira?: {carteira}")

apresentar2("Pedro", carteira=True, idade=25)

# "Pedro" foi passado de forma POSICIONAL.
# carteira=True e idade=25 foram passados de forma NOMEADA.


# Isto daria erro:
# apresentar2(carteira=True, "Pedro", idade=25)

# O motivo é que um argumento POSICIONAL ("Pedro")
# não pode aparecer depois de um argumento NOMEADO.


# PARÂMETROS COM VALORES PADRÃO
# Podemos definir um valor padrão para um parâmetro.
# Esse valor será utilizado caso nenhum argumento seja informado.

def operacao(num_a, num_b, div=1):
    return (num_a + num_b) / div

# Como não informamos "div", será usado o valor padrão: 1.
print(operacao(4, 2))

# Aqui informamos "div", então o valor padrão é substituído por 2.
print(operacao(4, 2, 2))

# Também podemos informar todos os parâmetros pelo nome.
print(operacao(div=2, num_a=7, num_b=7))

# IMPORTANTE:
# Parâmetros com valor padrão devem ficar depois dos parâmetros
# obrigatórios.
#
# Exemplo correto:
# def operacao(num_a, num_b, div=1):
#
# Exemplo incorreto:
# def operacao(div=1, num_a, num_b):


# *ARGS
# *args permite receber uma quantidade variável de argumentos.
# Todos os argumentos posicionais recebidos são armazenados em uma TUPLA.

def soma(*args):
    print(args[1])

# soma(1)
# Daria erro porque a tupla teria apenas:
# (1)
#
# O índice 1 não existe.

soma(1, 2, 3)
# args = (1, 2, 3)
# args[1] = 2

soma(1, 4, 5)
# args = (1, 4, 5)
# args[1] = 4

# soma()
# Também daria erro neste exemplo, pois args seria uma tupla vazia:
# ()


# **KWARGS
# **kwargs permite receber uma quantidade variável de argumentos
# NOMEADOS.
#
# Os argumentos recebidos são armazenados em um DICIONÁRIO.

def apresent(**kwargs):
    print(kwargs)

apresent(nome="João", idade=25, cidade="Londrina")

# kwargs será:
# {
#     "nome": "João",
#     "idade": 25,
#     "cidade": "Londrina"
# }


# UTILIZANDO *ARGS E **KWARGS JUNTOS
# *args recebe argumentos posicionais.
# **kwargs recebe argumentos nomeados.

def exemplo(*args, **kwargs):
    print("args:", args)
    print("**kwargs:", kwargs)

exemplo(10, 20, 30, nome="João", idade=25)

# args recebe:
# (10, 20, 30)
#
# kwargs recebe:
# {
#     "nome": "João",
#     "idade": 25
# }


# COMBINANDO PARÂMETROS
# Podemos combinar:
# 1. parâmetro normal
# 2. *args
# 3. parâmetros com valor padrão
# 4. **kwargs

def exemplo1(nome, *args, idade=18, **kwargs):

    print("nome:", nome)
    print("idade:", idade)
    print("args:", args)
    print("**kwargs:", kwargs)


exemplo1(
    "João",
    "Python",
    "Machine Learning",
    idade=25,
    cidade="Londrina",
    curso="TI"
)

# nome recebe "João".
#
# args recebe os argumentos posicionais restantes:
# ("Python", "Machine Learning")
#
# idade recebe 25.
#
# kwargs recebe os argumentos nomeados restantes:
# {
#     "cidade": "Londrina",
#     "curso": "TI"
# }


# ESCOPO
# Escopo determina onde uma variável pode ser acessada.
#
# Uma variável criada FORA de uma função pertence ao escopo externo
# (também chamado de escopo global).

mensagem = "Olá!"


def exemplo3():

    # A função consegue LER uma variável que foi criada fora dela.
    print(mensagem)


exemplo3()