# POO---Trabalho/services/gerenciar_atividade.py
from models.atividade import Atividade # Import the Atividade model

class GerenciarAtividade:
    def __init__(self): # Removed 'atividade' parameter here, as it's a manager
        self.atividades = [] # Initialize as an empty list to store Atividade objects

    def criar_atividade(self):
        print("\n--- CRIAR ATIVIDADE ---")
        nota = float(input("Nota da atividade: "))
        disciplina = input("Disciplina da atividade: ")
        professor_nome = input("Nome do professor responsável: ") # You'll need to link this to actual Professor objects later
        descricao = input("Descrição da atividade: ")

        # Create an instance of the Atividade model
        nova_atividade = Atividade(nota, disciplina, professor_nome, descricao)
        self.atividades.append(nova_atividade)
        print(f"Atividade '{descricao}' criada com sucesso!")

    def atualizar_atividade(self):
        print("\n--- ATUALIZAR ATIVIDADE ---")
        if not self.atividades:
            print("Nenhuma atividade cadastrada para atualizar.")
            return
        print("Atividades existentes:")
        for i, atv in enumerate(self.atividades, 1):
            print(f"{i}. {atv.descricao} (Nota: {atv.nota})")

        try:
            idx = int(input("Número da atividade a atualizar: ")) - 1
            if 0 <= idx < len(self.atividades):
                atividade_para_atualizar = self.atividades[idx]
                print(f"Atualizando: {atividade_para_atualizar.descricao}")
                novo_nota = float(input(f"Nova nota (atual: {atividade_para_atualizar.nota}): "))
                nova_disciplina = input(f"Nova disciplina (atual: {atividade_para_atualizar.disciplina}): ")
                novo_professor = input(f"Novo professor (atual: {atividade_para_atualizar.professor}): ")
                nova_descricao = input(f"Nova descrição (atual: {atividade_para_atualizar.descricao}): ")

                atividade_para_atualizar.nota = novo_nota
                atividade_para_atualizar.disciplina = nova_disciplina
                atividade_para_atualizar.professor = novo_professor
                atividade_para_atualizar.descricao = nova_descricao
                print("Atividade atualizada com sucesso!")
            else:
                print("Número de atividade inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")


    def excluir_atividade(self):
        print("\n--- EXCLUIR ATIVIDADE ---")
        if not self.atividades:
            print("Nenhuma atividade cadastrada para excluir.")
            return
        print("Atividades existentes:")
        for i, atv in enumerate(self.atividades, 1):
            print(f"{i}. {atv.descricao} (Nota: {atv.nota})")

        try:
            idx = int(input("Número da atividade a excluir: ")) - 1
            if 0 <= idx < len(self.atividades):
                removida = self.atividades.pop(idx)
                print(f"Atividade '{removida.descricao}' excluída com sucesso!")
            else:
                print("Número de atividade inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    # The validar_menu_atividades method should be part of MenuFunc, not GerenciarAtividade
    # as it deals with menu logic and authentication verification.