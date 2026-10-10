print("classes e objetos, programação orientada a objeto")

class Aluno():
    nome = ""
    idade = ""
    nota = 0
    anotacoes = ""
    ativo = True

    def ativar(self):
        self.ativo = True
    def desativar(self):
        self.ativo = False

    def aprovado(self):
        if self.nota >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

aluno1 = Aluno()
aluno1.nome = "Joaozinho"
aluno1.idade = "428"
aluno1.nota = 2.4
aluno1.anotacoes = "Joao"
aluno1.ativo = True

print(aluno1)

print("desativando aluno")
aluno1.desativar()

passou = aluno1.aprovado()
print(f"Situação do aluno: {passou}")