class Turma:
  alunos = []
  professores = []
  def __init__ (self, alunos, disciplina, professores):
    self._alunos = alunos
    self._disciplina = disciplina
    self._professores = professores
  
  @property
  def alunos(self):
    return self._alunos

  @alunos.setter
  def alunos(self, value):
    self._alunos = value

  @property
  def disciplina(self):
    return self._disciplina

  @disciplina.setter
  def disciplina(self, value):
    self._disciplina = value

  @property
  def professores(self):
    return self._professores

  @professores.setter
  def professores(self, value):
    self._professores = value