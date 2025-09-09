#                               EXERCICIO 01
#Eu, como dono de uma padaria, quero um sistema onde eu possa cadastrar meus produtos, alem de poder listar, alterar em caso de error, e excluir
#quando acabar o estoque. Quero tambem que tenha um menu onde eu possa ver as opções possiveis.

def menu():
    print("=== Menu padaria === \n")
    print("1 -cadastro \n")
    print("2 -lista \n")
    print("3 -alterar produto\n")
    print("4 -excluir produto \n")
    print("5 -sair \n")
    opcao =input("digite a opcao desejada: ")


    while opcao != "sair":
        
        if opcao == "1":
            cadastro()

        elif opcao == "2":
            lista()

        elif opcao =="3":
            alterarproduto()

        elif opcao == "4":
            excluirproduto()

        elif opcao == "sair":
            print("saindo...")

def cadastro():
    nome = input("Digite o cadastro: ")
    


def lista():
    lista = input("digite sua lista ")
    

def alterarproduto():
    print("alterar produto: ")


menu()





#                               EXERCICIO 02
#Sou dono de uma concessionaria e vi o sistema do dono da padaria. Gostaria de um sistema igual para meus carros.



#                               EXERCICIOS 03
#Explique poque quando tenho mais de um atributo(variavel), torna-se dificil/complicado o uso de arquivos.txt para guardar as informações.