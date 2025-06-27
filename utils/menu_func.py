from services.gerenciar_atividade import GerenciarAtividade
from services.gerenciar_pessoas import GerenciarAlunos, GerenciarProfessores
from services.gerenciar_turmas import GerenciarTurmas

class MenuFunc:
    def __init__(self):
        self.decision = None
        self.options = [
            ("Criar Atividade", GerenciarAtividade.criar_atividade),
            ("Atualizar Atividade", GerenciarAtividade.atualizar_atividade),
            ("Excluir Atividade", GerenciarAtividade.excluir_atividade),
            ("Adicionar Turma", GerenciarTurmas.adicionar_turma),
            ("Remover Turma", GerenciarTurmas.remover_turma),
            ("Listar Turmas", GerenciarTurmas.listar_turmas),
            ("Buscar Turma", GerenciarTurmas.buscar_turma),
            ("Cadastrar Aluno", GerenciarAlunos.adicionar_aluno),
            ("Listar Alunos", GerenciarAlunos.listar_alunos),
            ("Buscar Aluno", GerenciarAlunos.buscar_alunos),
            ("Atualizar Aluno", GerenciarAlunos.atualizar_aluno),
            ("Excluir Aluno", GerenciarAlunos.remover_aluno),
            ("Cadastrar Professor", GerenciarProfessores.adicionar_professor),
            ("Listar Professores", GerenciarProfessores.listar_professores),
            ("Buscar Professor", GerenciarProfessores.buscar_professores),
            ("Atualizar Professor", GerenciarProfessores.atualizar_professor),
            ("Excluir Professor", GerenciarProfessores.remover_professor),
            ("Sair", "Encerrar programa")
        ]

    def show_menu(self):
        print("\nMenu de Opções:")
        for index, (label, _) in enumerate(self.options):
            print(f"{index}. {label}")

    def get_decision(self):
        self.decision = input("Digite sua opção: ")
        return self.decision

    def start_decision(self):
        try:
            index = int(self.decision)
            name, function = self.options[index]
            if callable(function):
                function()
        except (ValueError, IndexError):
            print("Opção inválida!")