# class Pessoa:
#     pass

# pessoa = Pessoa()

# pessoa.nome = "Carlos"
# pessoa.idade = 25

# print(pessoa.nome)
# print(pessoa.idade) #Apesar de não ser boa prática, em python é possível criar objetos sem existirem na classe.

#Método construtor __init__
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa("Carlos", 25)

print(pessoa.nome)
print(pessoa.idade)

#Métodos 
class Pessoa1:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}!")

pessoa = Pessoa1("Carlos")

pessoa.apresentar()


class Pessoa2:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    def obter_idade(self):
        return self.idade

pessoa = Pessoa2("Carlos", 25)

pessoa.fazer_aniversario()

print(pessoa.obter_idade())

# Atributos e métodos de uma instância
class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def consultar_saldo(self):
        return self.saldo

conta = Conta("Carlos", 1000)

conta.depositar(500)

print(conta.consultar_saldo())

#Boas práticas
TAXA_DESCONTO = 0.10 #Constante


class CalculadoraPreco: #Classe CamelCase

    def __init__(self, preco): 
        self.preco = preco
        self._desconto = TAXA_DESCONTO #Atributo privado

    def calcular_preco_final(self): 
        return self.preco * (1 - self._desconto)
    