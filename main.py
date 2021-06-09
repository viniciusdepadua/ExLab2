from abc import ABC, abstractmethod


class Operacao(ABC):  # Command

    @abstractmethod
    def execute(self):
        pass


class VerificarSaldo(Operacao):  # ConcreteCommand

    def __init__(self):
        self.conta = conta

    def execute(self):
        self.conta.saldo()


class RealizarTransferencia(Operacao):  # ConcreteCommand
    def __init__(self):
        self.conta = conta

    def execute(self):
        self.conta.transferencia()


class VerificarExtrato(Operacao):  # ConcreteCommand

    def __init__(self):
        self.conta = conta

    def execute(self):
        self.conta.extrato()


class Conta:  # Receiver

    def extrato(self):
        print("Você verificará seu extrato")

    def transferencia(self):
        print("Você realizará uma transferência")

    def saldo(self):
        print("Você verificará seu saldo")


class Agent:  # Invoker

    def __init__(self):
        self.__operacao_queue = []

    def place_order(self, operacao):
        self.operacao = operacao
        operacao.execute()


# Cliente
conta = Conta()
verificar_extrato = VerificarExtrato()
verificar_saldo = VerificarSaldo()
realizar_transferencia = RealizarTransferencia()

# Invoker
agent = Agent()
agent.place_order(verificar_saldo)
agent.place_order(verificar_extrato)
agent.place_order(realizar_transferencia)
