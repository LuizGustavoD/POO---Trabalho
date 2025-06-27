# POO---Trabalho/services/gerenciar_turmas.py
from models.turma import Turma # Import Turma model

class GerenciarTurmas:
    def __init__(self): # Initialize without expecting 'turmas' initially
        self.turmas = []

    def adicionar_turma(self):
        print("\n--- ADICIONAR TURMA ---")
        # You'll need to gather input for alunos, disciplina, professores to create a Turma object
        # For a simple start, let's assume dummy values or prompt for basic info
        disciplina = input("Nome da disciplina da turma: ")
        # Dummy lists for now; in a real app, you'd select existing students/professors
        nova_turma = Turma(alunos=[], disciplina=disciplina, professores=[])
        self.turmas.append(nova_turma)
        print(f"Turma de '{disciplina}' adicionada com sucesso!")

    def remover_turma(self, turma_obj): # Should take a Turma object or identifier
        # This method needs to be robust, perhaps by name or ID
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
        # return self.turmas

    def buscar_turma(self, nome_turma):
        for turma in self.turmas:
            if turma.disciplina == nome_turma: # Assuming 'disciplina' is used as name
                return turma
        return None

    # Remove validar_menu_turmas as authentication should be in MenuFunc