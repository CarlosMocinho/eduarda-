# Definição da classe Cabeca
class Cabeca:
    def _init_(self):
        # Inicializa o atributo estado como "Intacta"
        self.estado = "Intacta"

    def destruir(self):
        # Muda o estado para "Destruída" quando o método destruir é chamado
        self.estado = "Destruída"
        # Imprime uma mensagem informando que a cabeça foi destruída
        print("A cabeça foi destruída!")

# Definição da classe Boneco
class Boneco:
    def _init_(self):
        # Inicializando o atributo cabeca como uma instância da classe Cabeca
        self.cabeca = Cabeca()

    def destruir(self):
        # Chama o método destruir da instância de Cabeca associada ao boneco
        self.cabeca.destruir()
        # Imprime uma mensagem informando que o boneco foi destruído

# Bloco de código a ser executado apenas se este arquivo for executado diretamente
if _name_ == "_main_":
    # Cria um objeto da classe Boneco
    boneco = Boneco()
    # Chama o método destruir do boneco, que também chama o método destruir da cabeça
    boneco.destruir()