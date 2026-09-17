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

# if __name__ == "__main__":        
#     Turma = { "alunos": [Aluno("Náthally", [10,10,10]),  Aluno("João", [20,10,50])]}
#     for aluno in Turma["alunos"]:
#         aluno.apresentar_aluno()

        
Turma = { "alunos": [Aluno("Náthally", [10,10,10]),  Aluno("João", [20,10,50])]}
for aluno in Turma["alunos"]:
    aluno.apresentar_aluno()
    