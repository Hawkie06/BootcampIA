# Crie um sistema para cadastrar alunos de uma turma, deve conter nas informação
# dos alunos o nome e as notas de cada disciplina. Aluno deve ser uma classe para
# salvar as informações, e deverá ter um método para calcular o coeficiente do aluno,
# e outro para printar as informações do aluno com o nome, o nome de cada
# disciplina com a nota do aluno, e o coeficiente.

class Aluno:
    DISCIPLINAS = ["Matemática", "Português", "Geografia"]

    def __init__(self, aluno, nota):
        self.aluno = aluno
        self.nota = nota
        
    def calcular_media(self):
        resultado = 0
        for i in self.nota:
            resultado = resultado + i
        return resultado / len(self.nota)

    def apresentar_aluno(self):
        print(f"O nome do aluno é: {self.aluno}")

        mydict = {}
        for i, chave in enumerate(self.DISCIPLINAS):
            mydict[chave] = self.nota[i] 

        print(f"Disciplinas e notas: {mydict}")   
        print(f"A média dele é: {self.calcular_media():.2f}")
        

Turma = { "alunos": [Aluno("Náthally", [10,10,10]),  Aluno("João", [20,10,50])]}
for aluno in Turma["alunos"]:
    aluno.apresentar_aluno()