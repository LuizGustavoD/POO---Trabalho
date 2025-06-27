from datetime import datetime
from models.pessoa import Pessoa 
from models.atividade import Atividade

class Aluno(Pessoa):

  def __init__(self, nome, idade, matricula, atividades):
    super().__init__(nome, idade)
    self._atividades = atividades
    self._matricula = matricula
    self._data_cadastro = datetime.now()

  def __str__(self):
    return f"Aluno: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}, Atividades: {self.atividades}, Data de Cadastro: {self.data_cadastro}"

  @property
  def nome(self):
    return self._nome

  @property
  def idade(self):
    return self._idade

  @property
  def matricula(self):
    return self._matricula

  @property
  def data_cadastro(self):
    return self._data_cadastro

  @property
  def atividades(self):
    return self._atividades

  @nome.setter
  def nome(self, novo_nome):
    self._nome = novo_nome

  @idade.setter
  def idade(self, nova_idade):
    if nova_idade < 0:
      raise ValueError("Idade não pode ser negativa.")
    self._idade = nova_idade

  @matricula.setter
  def matricula(self, nova_matricula):
    if not nova_matricula:
      raise ValueError("Matrícula não pode ser vazia.")
    self._matricula = nova_matricula

  @atividades.setter
  def atividades(self, novas_atividades):
    if not novas_atividades:
      raise ValueError("Atividades não podem ser vazias.")
    self._atividades = novas_atividades