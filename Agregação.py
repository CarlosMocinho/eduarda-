class Monitor:
    def _init_(self, modelo, cor, tamanho):
        #Define as características.
        self.modelo = modelo
        self.cor = cor

    def informacoes_monitor(self):
        #Mostra as informações de monitor.
        print(f"Monitor {self.modelo} da cor {self.cor}")

class Computador:
    def _init_(self, nome, monitor=None):
        #Define informações de computador e qual monitor ele possui.
        self.nome = nome
        self.monitor = monitor

    def conectar_monitor(self, monitor):
        #Conecta um monitor.
        self.monitor = monitor

    def informacoes_monitor(self):
        #Mostra informações de um computador e de monitor.
        if self.monitor:
            print(f"Computador {self.nome} com o seguinte monitor:")
            self.monitor.informacoes_monitor()
        else:
            print(f"Computador {self.nome} não possui monitor")

#Criação dos objetos e cumprimento dos métodos.
monitor1 = Monitor("Dell", 23)
computador1 = Computador("Inter Core I5")
computador1.conectar_monitor(monitor1)
monitor2 = Monitor("LG", 27)
computador2 = Computador("Desktop")
computador1.informacoes_monitor()
computador2.informacoes_monitor()