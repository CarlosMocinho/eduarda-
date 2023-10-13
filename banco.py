class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente para efetuar o saque.")
            return False

    def ver_saldo(self):
        print(f"Saldo atual da conta de {self.titular}: R${self.saldo:.2f}")

conta_joao = ContaBancaria("João")

while True:
    print("\nEscolha uma opção:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver Saldo")
    print("4 - Sair")
    
    escolha = input("Opção: ")

    if escolha == "1":
        valor = float(input("Digite o valor a ser depositado: "))
        conta_joao.depositar(valor)
        print(f"R${valor:.2f} depositado na conta.")
    elif escolha == "2":
        valor = float(input("Digite o valor a ser sacado: "))
        if conta_joao.sacar(valor):
            print(f"R${valor:.2f} sacado da conta.")
    elif escolha == "3":
        conta_joao.ver_saldo()
    elif escolha == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")
