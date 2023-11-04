# Definição da classe Curso
class Curso:
    # Método construtor dessa classe
    def _init_(self, nome, codigo):
        # Inicializa o atributo nome
        self.nome = nome
        # Inicializando o atributo código
        self.codigo = codigo
        # Inicializando o atributo professor usando None
        self.professor = None

    # Método para designar um professor ao curso
    def designar_professor(self, professor):
        # Atribuindo professor ao atributo professor do curso
        self.professor = professor

# Definição da classe Professor
class Professor:
    # Método que constrói a classe Professor
    def _init_(self, nome, matricula):
        # Inicializando o atributo nome
        self.nome = nome
        # Inicializando o atributo matricula 
        self.matricula = matricula
        # Inicializando o atributo cursos como uma lista vazia
        self.cursos = []

    # Método para que um professor lecione um curso
    def lecionar_curso(self, curso):
        # Adicionando curso à lista de cursos que o professor pode lecionar
        self.cursos.append(curso)

    # Método para listar os cursos que um professor leciona
    def listar_cursos(self):
        # Imprime uma mensagem com o nome do professor
        print(f"O professor {self.nome} leciona tais cursos:")
        # Percorre a lista de cursos e imprime seus nomes e códigos
        for curso in self.cursos:
            print(f"- {curso.nome} ({curso.codigo})")

# Criação de objetos da classe Curso com nomes e códigos específicos
curso1 = Curso("Python", "001")
curso2 = Curso("Banco de Dados", "002")
curso3 = Curso("Redes", "003")

# Criação de dois objetos da classe Professor com nomes e matrículas específicas
prof_1 = Professor("Diemes", "100")
prof_2 = Professor("Giulios", "101")
prof_3 = Professor("Paulinho", "102")

# Associação de professores aos cursos
curso1.designar_professor(prof_1)
curso2.designar_professor(prof_2)
curso3.designar_professor(prof_3)

# Associando cursos a professores
prof_1.lecionar_curso(curso1)
prof_1.lecionar_curso(curso3)
prof_2.lecionar_curso(curso2)

# Listagem dos cursos lecionados por cada professor
prof_1.listar_cursos()
prof_2.listar_cursos()