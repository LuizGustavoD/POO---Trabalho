from datetime import datetime
from models.pessoa import Pessoa  # Corrected import from previous issue
from models.atividade import Atividade # Assuming Atividade class is in models/atividade.py

class Aluno(Pessoa):
  # Removed the class attribute 'atividades = []' as it's likely not intended for instance-specific activities.
  def __init__(self, nome, idade, matricula, atividades):
    super().__init__(nome, idade)
    self._atividades = atividades # Changed to _atividades for consistency (plural for a list)
    self._matricula = matricula
    self._data_cadastro = datetime.now()

  def __str__(self):
    # Updated the string representation to use 'Atividades'
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

  # Added the getter for the 'atividades' property
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

  # Corrected the setter to match the 'atividades' property
  @atividades.setter
  def atividades(self, novas_atividades):
    if not novas_atividades:
      raise ValueError("Atividades não podem ser vazias.")
    self._atividades = novas_atividades