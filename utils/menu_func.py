from services.gerenciar_atividade import GerenciarAtividade
from services.gerenciar_pessoas import GerenciarAlunos, GerenciarProfessores
from services.gerenciar_turmas import GerenciarTurmas
from models.atividade import Atividade

class MenuFunc:
    def __init__(self):
        self.decision = None

        self.gerenciar_alunos = GerenciarAlunos()
        self.gerenciar_professores = GerenciarProfessores()
        self.gerenciar_atividade = GerenciarAtividade()
        self.gerenciar_turmas = GerenciarTurmas()

        # Menus públicos
        self.menu_publico = [
            ("Gerenciar Alunos", lambda: self.exibir_sub_menu(self.menu_aluno)),
            ("Gerenciar Professores", lambda: self.exibir_sub_menu(self.menu_professor)),
            ("Gerenciar Atividades (acesso restrito)", self.autenticar_menu_atividades),
            ("Gerenciar Turmas (acesso restrito)", self.autenticar_menu_turmas),
            ("Sair", None)
        ]

        # Menus internos
        self.menu_aluno = [
            ("Adicionar aluno", self.gerenciar_alunos.adicionar_aluno),
            ("Remover aluno", self.gerenciar_alunos.remover_aluno),
            ("Listar alunos", self.gerenciar_alunos.listar_alunos),
            ("Voltar", None)
        ]

        self.menu_professor = [
            ("Adicionar professor", self.gerenciar_professores.adicionar_professor),
            ("Remover professor", self.gerenciar_professores.remover_professor),
            ("Listar professores", self.gerenciar_professores.listar_professores),
            ("Voltar", None)
        ]

        self.menu_atividades = [
            ("Criar atividade", self.gerenciar_atividade.criar_atividade),
            ("Atualizar atividade", self.gerenciar_atividade.atualizar_atividade),
            ("Excluir atividade", self.gerenciar_atividade.excluir_atividade),
            ("Voltar", None)
        ]

        self.menu_turmas = [
            ("Adicionar turma", self.gerenciar_turmas.adicionar_turma),
            ("Remover turma", self.gerenciar_turmas.remover_turma),
            ("Listar turmas", self.gerenciar_turmas.listar_turmas),
            ("Voltar", None)
        ]

    def executar(self):
        while True:
            print("\n=== SISTEMA DE GESTÃO ESCOLAR ===")
            self.exibir_menu(self.menu_publico)
            opcao_func = self.pegar_opcao(self.menu_publico)
            if opcao_func is None:
                print("\nSaindo do sistema... Até logo!")
                break
            opcao_func()

    def exibir_menu(self, opcoes):
        for i, (titulo, _) in enumerate(opcoes):
            print(f"{i + 1}. {titulo}")

    def exibir_sub_menu(self, sub_opcoes):
        while True:
            self.exibir_menu(sub_opcoes)
            opcao_func = self.pegar_opcao(sub_opcoes)
            if opcao_func is None:
                break
            opcao_func()

    def pegar_opcao(self, opcoes):
        try:
            escolha = int(input("Escolha uma opção: ")) - 1
            if 0 <= escolha < len(opcoes):
                return opcoes[escolha][1]
        except ValueError:
            pass
        print("Opção inválida!")
        return self.pegar_opcao(opcoes)

    def autenticar_menu_atividades(self):
        if self.gerenciar_professores.verificar_professor():
            self.exibir_sub_menu(self.menu_atividades)
        else:
            print("Acesso negado. Apenas professores autenticados podem gerenciar atividades.")


    def autenticar_menu_turmas(self):
        if self.gerenciar_professores.verificar_professor():
            self.exibir_sub_menu(self.menu_turmas)
        else:
            print("Acesso negado. Apenas professores autenticados podem gerenciar turmas.")


if __name__ == "__main__":
    sistema = MenuFunc()
    sistema.executar()