class Pessoa:
  def __init__(self, nome, idade):
    self._nome = nome
    self._idade = idade

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
