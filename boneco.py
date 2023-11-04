class Cabeca:
    def __init__(self, cor):
        self.cor = cor

class Boneco:
    def __init__(self, nome, cor_cabeca):
        self.nome = nome
        self.cabeca = Cabeca(cor_cabeca)

    def destruir(self):
        print(f'O boneco {self.nome} foi destruído.')
        del self.cabeca
        print('A cabeça do boneco também foi destruída.')