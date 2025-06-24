class GerenciarTurmas:
    def __init__(self, turmas):
        self.turmas = turmas

    def adicionar_turma(self, turma):
        self.turmas.append(turma)

    def remover_turma(self, turma):
        if turma in self.turmas:
            self.turmas.remove(turma)

    def listar_turmas(self):
        return self.turmas

    def buscar_turma(self, nome_turma):
        for turma in self.turmas:
            if turma.nome == nome_turma:
                return turma
        return None