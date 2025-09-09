#                               EXERCICIO 01
#Eu, como dono de uma padaria, quero um sistema onde eu possa cadastrar meus produtos, alem de poder listar, alterar em caso de error, e excluir
#quando acabar o estoque. Quero tambem que tenha um menu onde eu possa ver as opções possiveis.

def carregarArquivo():
    try:
        with open('padaria.txt', 'r') as arquivo: 
            lista = arquivo.readlines()
    except FileNotFoundError:
        print("Arquivo não encontrado")

def menu():
    carregarArquivo()
    print("=== Menu Padaria === \n")
    print("1 -cadastro \n")
    print("2 -lista \n")
    print("3 - alterar produto \n")
    print("4 - excluir produto \n")
    print("5 - sair")
    opcao = input ("digite a opcao desejada: ")


    while opcao != "sair":
        
        if opcao == "1":
            cadastro()
            menu()

        elif opcao == "2":
            lista() 
            menu()

        elif opcao == "3":   
            alterar_produto()
            menu()

        elif opcao == "4":
            excluir()
            menu()

        elif opcao == "sair" :
            print("saindo...")   
            break   


def cadastro():   
    lista = []
    nome = input ("digite o nome do produto: ")
    lista.append(nome)

    with open('padaria.txt', 'w') as arquivo: 
        arquivo.writelines(lista)
        

def lista():
    lista = []
    with open('padaria.txt', 'r') as arquivo: 
            lista = arquivo.readlines()
            print(lista)
    

def alterar_produto():
    produto_alterar = input("Digite o nome do produto para alterar:\n").strip()
    
    with open('padaria.txt', 'r') as arquivo:
        lista = arquivo.readlines()

    nova_lista = []

    for linha in lista:
        if linha.strip() == produto_alterar:
            novo_nome = input("Digite o novo nome do produto:\n").strip()
            nova_lista.append(novo_nome)

    with open('padaria.txt', 'w') as arquivo:
        arquivo.writelines(nova_lista)
        print("Produto alterado com sucesso!")
    
    
def excluir():
    produto_excluir = input("Digite o nome do produto para excluir:\n").strip()
    
    with open('padaria.txt', 'r') as arquivo:
        lista = arquivo.readlines()

    nova_lista = []

    for linha in lista:
        if linha.strip() != produto_excluir:
            nova_lista.append(linha)

    with open('padaria.txt', 'w') as arquivo:
        arquivo.writelines(nova_lista)
        print("Produto excluído com sucesso!")
    


menu()


with open('arquivo.txt', 'r') as file: dados = files.readlines()



#                               EXERCICIO 02
#Sou dono de uma concessionaria e vi o sistema do dono da padaria. Gostaria de um sistema igual para meus carros.

def carregarArquivo():
    try:
        with open('concessionaria.txt', 'r') as arquivo: 
            lista = arquivo.readlines()
    except FileNotFoundError:
        print("Arquivo não encontrado")

def menu():
    carregarArquivo()
    print("=== Menu concessionaria === \n")
    print("1 -cadastro \n")
    print("2 -lista \n")
    print("3 - alterar produto \n")
    print("4 - excluir produto \n")
    print("5 - sair")
    opcao = input ("digite a opcao desejada: ")


    while opcao != "sair":
        
        if opcao == "1":
            cadastro()
            menu()

        elif opcao == "2":
            lista() 
            menu()

        elif opcao == "3":   
            alterar_produto()
            menu()

        elif opcao == "4":
            excluir()
            menu()

        elif opcao == "sair" :
            print("saindo...")   
            break   


def cadastro():   
    lista = []
    nome = input ("digite o nome do produto: ")
    lista.append(nome)

    with open('concessionaria.txt', 'w') as arquivo: 
        arquivo.writelines(lista)
        

def lista():
    lista = []
    with open('concessionaria.txt', 'r') as arquivo: 
            lista = arquivo.readlines()
            print(lista)
    

def alterar_produto():
    produto_alterar = input("Digite o nome do produto para alterar:\n").strip()
    
    with open('concessionaria.txt', 'r') as arquivo:
        lista = arquivo.readlines()

    nova_lista = []

    for linha in lista:
        if linha.strip() == produto_alterar:
            novo_nome = input("Digite o novo nome do produto:\n").strip()
            nova_lista.append(novo_nome)

    with open('concessionaria.txt', 'w') as arquivo:
        arquivo.writelines(nova_lista)
        print("Produto alterado com sucesso!")
    
    
def excluir():
    produto_excluir = input("Digite o nome do produto para excluir:\n").strip()
    
    with open('concessionaria.txt', 'r') as arquivo:
        lista = arquivo.readlines()

    nova_lista = []

    for linha in lista:
        if linha.strip() != produto_excluir:
            nova_lista.append(linha)

    with open('concessionaria.txt', 'w') as arquivo:
        arquivo.writelines(nova_lista)
        print("Produto excluído com sucesso!")
    


menu()


with open('arquivo.txt', 'r') as file: dados = files.readlines()



#                               EXERCICIOS 03
#Explique poque quando tenho mais de um atributo(variavel), torna-se dificil/complicado o uso de arquivos.txt para guardar as informações.