class GerenciarAlunos:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)

    def listar_alunos(self):
        return self.alunos


class GerenciarProfessores:
    def __init__(self):
        self.professores = []

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def remover_professor(self, professor):
        if professor in self.professores:
            self.professores.remove(professor)

    def listar_professores(self):
        return self.professores