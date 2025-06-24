class MenuFunc:
    decisao = None
    def show_menu(self):
        print("Menu de Opções:")
        print("1. Criar Atividade")
        print("2. Atualizar Atividade")
        print("3. Excluir Atividade")
        print("4. Adicionar Turma")
        print("5. Remover Turma")
        print("6. Listar Turmas")
        print("7. Buscar Turma")
        print("8. Cadastrar Aluno")
        print("9. Listar Alunos")
        print("10. Buscar Aluno")
        print("11. Atualizar Aluno")
        print("12. Excluir Aluno")
        print("13. Cadastrar Professor")
        print("14. Listar Professores")
        print("15. Buscar Professor")
        print("16. Atualizar Professor")
        print("17. Excluir Professor")
        print("0. Sair")

    def get_decision(self):
        self.decisao = input("Digite sua opção: ")
        return self.decisao
    
    