class Disciplina:
    atividades = []
    def __init__ (self, professor, atividades):
        self._professor = professor
        self._atividades = atividades
        
    @property
    def professor(self):
      return self._professor

    @professor.setter
    def professor(self, value):
      self._professor = value

    @property
    def atividades(self):
      return self._atividades

    @atividades.setter
    def atividades(self, value):
      self._atividades = value

    @classmethod
    def get_atividades(cls):
      return cls.atividades

    @classmethod
    def set_atividades(cls, atividades):
      cls.atividades = atividades