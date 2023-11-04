class Monitor:
    def __init__(self, marca):
        self.marca = marca
        self.computador = None

class Computador:
    def __init__(self, modelo):
        self.modelo = modelo
        self.monitor = None

    def conectar(self, monitor):
        self.monitor = monitor
        monitor.computador = self