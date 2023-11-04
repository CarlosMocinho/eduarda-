class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []

    def lecionar(self, curso):
        self.cursos.append(curso)
        curso.professor = self

    def listar_cursos(self):
        return [curso.nome for curso in self.cursos]


class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.professor = None