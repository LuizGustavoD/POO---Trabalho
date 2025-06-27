class MenuFunc:
    def __init__(self):
        self.decision = None
        self.options = [
            ("Sair", ""),
            ("Criar Atividade", self.criar_atividade),
            ("Atualizar Atividade", self.atualizar_atividade),
            ("Excluir Atividade", self.excluir_atividade),
            ("Adicionar Turma", self.adicionar_turma),
            ("Remover Turma", self.remover_turma),
            ("Listar Turmas", self.listar_turmas),
            ("Buscar Turma", self.buscar_turma),
            ("Cadastrar Aluno", self.cadastrar_aluno),
            ("Listar Alunos", self.listar_alunos),
            ("Buscar Aluno", self.buscar_aluno),
            ("Atualizar Aluno", self.atualizar_aluno),
            ("Excluir Aluno", self.excluir_aluno),
            ("Cadastrar Professor", self.cadastrar_professor),
            ("Listar Professores", self.listar_professores),
            ("Buscar Professor", self.buscar_professor),
            ("Atualizar Professor", self.atualizar_professor),
            ("Excluir Professor", self.excluir_professor),
        ]

    def show_menu(self):
        for index, (option, func) in enumerate(self.options):
            print(f"{index}. {option}")

    def get_decision(self):
        self.decision = input("Digite sua opção: ")
        return self.decision

    def start_decision(self):
        try:
            name, function = self.options[int(self.decision)]
            function()
        except (ValueError, IndexError):
            print("Opção inválida!")

    def criar_atividade(self): print("Criando atividade...")
    def atualizar_atividade(self): print("Atualizando atividade...")
    def excluir_atividade(self): print("Excluindo atividade...")
    def adicionar_turma(self): print("Adicionando turma...")
    def remover_turma(self): print("Removendo turma...")
    def listar_turmas(self): print("Listando turmas...")
    def buscar_turma(self): print("Buscando turma...")
    def cadastrar_aluno(self): print("Cadastrando aluno...")
    def listar_alunos(self): print("Listando alunos...")
    def buscar_aluno(self): print("Buscando aluno...")
    def atualizar_aluno(self): print("Atualizando aluno...")
    def excluir_aluno(self): print("Excluindo aluno...")
    def cadastrar_professor(self): print("Cadastrando professor...")
    def listar_professores(self): print("Listando professores...")
    def buscar_professor(self): print("Buscando professor...")
    def atualizar_professor(self): print("Atualizando professor...")
    def excluir_professor(self): print("Excluindo professor...")

