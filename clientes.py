class Cliente:
    def _init_(self, nome, CPF):
        self.nome = nome
        self.CPF = CPF
        self.contas = []

    def abrir_conta(self, id, tipo, saldo_inicial = 0):
        self.id = id
        self.tipo = tipo
        self.saldo_inicial = saldo_inicial
