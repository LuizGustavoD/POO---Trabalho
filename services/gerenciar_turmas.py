from models.turma import Turma

class GerenciarTurmas:
    def __init__(self):
        self.turmas = []

    def adicionar_turma(self):
        print("\n--- ADICIONAR TURMA ---")
        disciplina = input("Nome da disciplina da turma: ")

        nova_turma = Turma(alunos=[], disciplina=disciplina, professores=[])
        self.turmas.append(nova_turma)
        print(f"Turma de '{disciplina}' adicionada com sucesso!")

    def remover_turma(self, turma_obj):
        if turma_obj in self.turmas:
            self.turmas.remove(turma_obj)
            print("Turma removida com sucesso!")
        else:
            print("Turma não encontrada.")

    def listar_turmas(self):
        print("\n--- LISTA DE TURMAS ---")
        if not self.turmas:
            print("Nenhuma turma cadastrada.")
            return
        for i, turma in enumerate(self.turmas, 1):
            print(f"{i}. Disciplina: {turma.disciplina}, Alunos: {len(turma.alunos)}, Professores: {len(turma.professores)}")

    def buscar_turma(self, nome_turma):
        for turma in self.turmas:
            if turma.disciplina == nome_turma:
                return turma
        return None