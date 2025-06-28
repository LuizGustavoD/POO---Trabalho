from models.pessoa import Pessoa

class Professor (Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self._disciplina = disciplina

    def __str__(self):
        return f"Professor: {self.nome}, Idade: {self.idade}, Disciplina: {self.disciplina}"

    @property
    def disciplina(self):
        return self._disciplina

    @disciplina.setter
    def disciplina(self, nova_disciplina):
        if not nova_disciplina:
            raise ValueError("Disciplina não pode ser vazia.")
        self._disciplina = nova_disciplina  
    @property
    def nome(self): 
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            raise ValueError("Idade não pode ser negativa.")
        self._idade = nova_idade