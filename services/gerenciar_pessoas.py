# POO---Trabalho/services/gerenciar_pessoas.py
from models.aluno import Aluno
from models.professor import Professor

class GerenciarAlunos:
    def __init__(self):
        self.alunos = [] 

    def adicionar_aluno(self):
        print("\n--- ADICIONAR ALUNO ---")
        nome = input("Nome do aluno: ")
        idade = int(input("Idade do aluno: "))
        matricula = input("Matrícula do aluno: ") 

        self.alunos.append(Aluno(nome, idade, matricula, []))
        print(f"Aluno '{nome}' adicionado com sucesso!")

    def remover_aluno(self):
        print("\n--- REMOVER ALUNO ---")
        matricula = input("Matrícula do aluno a remover: ")
        original_len = len(self.alunos)
        self.alunos = [aluno for aluno in self.alunos if aluno.matricula != matricula]
        if len(self.alunos) < original_len:
            print(f"Aluno com matrícula '{matricula}' removido.")
        else:
            print(f"Aluno com matrícula '{matricula}' não encontrado.")

    def listar_alunos(self):
        print("\n--- LISTA DE ALUNOS ---")
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
            return
        for aluno in self.alunos:
            print(aluno)

    def buscar_alunos(self):

        pass

    def atualizar_aluno(self):

        pass


class GerenciarProfessores:
    def __init__(self):
        self.professores = []
        self.professor_autenticado = None

    def adicionar_professor(self):
        print("\n--- ADICIONAR PROFESSOR ---")
        nome = input("Nome do professor: ")
        idade = int(input("Idade do professor: "))
        materia = input("Matéria que leciona: ")
        self.professores.append(Professor(nome, idade, materia))
        print(f"Professor '{nome}' adicionado com sucesso!")

    def remover_professor(self):
        print("\n--- REMOVER PROFESSOR ---")
        nome = input("Nome do professor a remover: ")
        original_len = len(self.professores)
        self.professores = [prof for prof in self.professores if prof.nome != nome]
        if len(self.professores) < original_len:
            print(f"Professor '{nome}' removido.")
        else:
            print(f"Professor '{nome}' não encontrado.")

    def verificar_professor(self):
        print("\n--- AUTENTICAÇÃO DE PROFESSOR ---")
        nome = input("Nome do professor: ").strip()
        if not nome:
            print("Nome não pode estar vazio!")
            return False
        for professor in self.professores:
            if professor.nome.lower() == nome.lower():
                self.professor_autenticado = professor.nome
                print(f"Bem-vindo, professor {professor.nome}!")
                return True
        print("Professor não encontrado!")
        return False

    def listar_professores(self):
        print("\n--- LISTA DE PROFESSORES ---")
        if not self.professores:
            print("Nenhum professor cadastrado.")
            return
        for professor in self.professores:
            print(professor)
        
    def buscar_professores(self):
        # Implementation for searching
        pass

    def atualizar_professor(self):
        # Implementation for updating
        pass