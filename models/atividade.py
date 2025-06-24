class Atividade:
  def __init__(self, nota, disciplina, professor, descricao):
    self._nota = nota
    self._disciplina = disciplina
    self._professor = professor
    self._descricao = descricao
  
  def __str__(self):
    return f"Atividade: {self.descricao}, Nota: {self.nota}, Disciplina: {self.disciplina}, Professor: {self.professor}"
  
  @property
  def nota(self):
    return self._nota

  @nota.setter
  def nota(self, value):
    self._nota = value

  @property
  def disciplina(self):
    return self._disciplina

  @disciplina.setter
  def disciplina(self, value):
    self._disciplina = value

  @property
  def professor(self):
    return self._professor

  @professor.setter
  def professor(self, value):
    self._professor = value

  @property
  def descricao(self):
    return self._descricao

  @descricao.setter
  def descricao(self, value):
    self._descricao = value