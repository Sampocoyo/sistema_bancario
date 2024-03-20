from clientes import Cliente
from conta import Conta
from conta_poupanca import Conta_Poupanca

print ("Bem Vindo ao Banco Money Na Nuvem, número 1 em satisfação dos clientes \n")
print('Entre no nosso sistema! ')

n = input("Digite seu nome: ")
cpf = input ("Digite seu CPF: ")
cont = 0

cliente1 = Cliente (n, cpf)
resposta = input("Você deseja abrir uma conta? Reponda com 'sim' ou 'não: ")
while cont < 1:
    if resposta.capitalize == "Sim":
        t = input("Digite qual o tipo de conta você deseja abrir? Deve ser 'poupança' ou 'corrente': ")
        break
    else:
        print ('Ok, você pode abrir sua conta depois!')
        resposta = input("Você deseja abrir uma conta? Reponda com 'sim' ou 'não: ")


if t.capitalize == "Corrente":
    id = input("Digte o seu ID: ")
    c_corrente = cliente1.abrir_conta(id,t)

elif t.capitalize == "Poupança":
    id = input("Digte o seu ID: ")
    c_poupanca = cliente1.abrir_conta(id,t)
else:
    print ('Tipo de conta inválido')

c_corrente = Conta
c_corrente.depositar()
c_corrente.sacar()

c_poupanca = Conta.depositar()
c_poupanca = Conta_Poupanca.mostrar_juros()
c_poupanca = Conta.sacar()
