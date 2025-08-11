#criar funcao menu de opcoes e pedir a opcao desejada ao usuario 
#criar funcao de deposito
#criar funcao de saque
#criar funcao de ver saldo
#ao digitar "sair" encerrar o programa
saldo = 0

def menu():
    print("=== Menu de Opções === \n")
    print("1 -Depositar \n")
    print("2 -Saque \n")
    print("3 -Saldo \n")
    print("4 -Sair \n")
    opcao =input("digite a opcao desejada: ")

    while opcao != "sair":
        
        if opcao == "1":
            depositar(saldo)

        elif opcao == "2":
            saque(saldo)

        elif opcao =="3":
            verSaldo(saldo)

        elif opcao == "sair":
            print("saindo...")

def depositar(saldo):
    valor = input("Digite o valor do depósito: ")
    saldo += valor


def saque(saldo):
    valor = input("digite seu saque: ")
    saldo -= valor 


def verSaldo(saldo):
    print("seu saldo e: ", saldo)


