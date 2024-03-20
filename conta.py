class Conta: 
    def _init_(self, id, nome, CPF, tipo, saldo=0):
        self.id = id
        self.nome = nome
        self.CPF = CPF
        self.saldo = saldo
        self.tipo = tipo
        self.transacao = []

    def depositar (self):
        valor = float(input('Digite o valor para depositar: '))
        if(valor <=0):
            print("Valor inválido para depósito.")
        else:
            self.saldo += valor
            print("Seu Depósito foi de: ", valor)
            return self.saldo
            
    def sacar(self):
        valor = float(input('Digite o valor para sacar: '))
        if self.saldo >= valor:
            self.saldo -= valor
            self.registro_transacoes (valor," - Saque")
        else:
            print ("Saldo insuficiente!")
        
    def registro_transacoes(self, valor, tipo):
        self.transacao.append({'Tipo': tipo, 'Valor': valor})

    def exibir_extrato (self):
        print("Extrato da Conta ", self.id)
        print("Saldo:  R$", self.saldo)
        print("Transações: ")
        for transacoes in self.transacao:
            print(transacoes)