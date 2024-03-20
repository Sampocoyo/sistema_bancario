from conta import Conta

class Conta_Poupanca:
    def __init__(self, id, nome, CPF, saldo, tipo = 'Poupança', taxa_juros = 5/100):
        self.taxa_juros = taxa_juros
        super().__init__(id, nome, CPF, tipo, saldo)
    
    def mostrar_juros(self):
        mostrar = float((self.saldo * self.taxa_juros) - self.saldo)
        valor_poupanca = ((self.saldo * self.taxa_juros) + self.saldo)
        print ('O saldo da conta poupança é: R${}'.format(valor_poupanca))
        print ('O valor do juro da conta poupança é: R${}'.format(mostrar))
    