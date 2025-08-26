# 1 usando(laços, funçao e try/except),crie um sistema
# para receber as 3 notas de um aluno e calcule a media 
# anual, se digitar algo sem ser numero tratar o erro
 
def calcular_media(notas):
     return sum(notas) / len(notas)

notas = []
contador = 1

while contador <= 3:
    try:
        nota = float(input(f"Digite a {contador}ª nota do aluno: "))
        if nota < 0 or nota > 10:
            print("Nota inválida! Digite uma nota entre 0 e 10.")
            continue
        notas.append(nota)
        contador += 1
    except ValueError:
        print("Entrada inválida! Por favor, digite um número.")

media = calcular_media(notas)
print(f"Média anual do aluno: {media:.2f}")
 
# 2 usando (lista, funçao, laços, try/except), voce devera
#criar uma lista com numeros, adicionar a uma lista a parte
#se for mensagem, tratar com o erro de tipo. ao final, mostar
# a lista so com os numeros 

def tentar_converter_para_numero(valor):
    try:
        return float(valor)
    except ValueError:
        raise TypeError("Não é um número.")

lista_entrada = []
lista_numeros = []

while True:
    dado = input("Digite um valor (ou 'sair' para encerrar): ")
    if dado.lower() == "sair":
        break
    lista_entrada.append(dado)

for item in lista_entrada:
    try:
        numero = tentar_converter_para_numero(item)
        lista_numeros.append(numero)
    except TypeError:
        print(f"Ignorado: '{item}' não é número.")

print("\n📋 Lista com os números digitados:")
print(lista_numeros)


# 3 criar uma lista com cadastro d usuario
# - castrar, alterar, excluir, listar
# usar (funçao, lista, try/except,laços)


usuarios = []

def cadastrar_usuario():
    try:
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        email = input("Digite o email do usuário: ")
        usuario = {"nome": nome, "idade": idade, "email": email}
        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!\n")
    except ValueError:
        print("Erro: Idade deve ser um número.\n")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
        return
    print("=== Lista de Usuários ===")
    for i, usuario in enumerate(usuarios):
        print(f"{i} - Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}")
    print()

def alterar_usuario():
    listar_usuarios()
    try:
        indice = int(input("Digite o número do usuário que deseja alterar: "))
        if 0 <= indice < len(usuarios):
            nome = input("Novo nome: ")
            idade = int(input("Nova idade: "))
            email = input("Novo email: ")
            usuarios[indice] = {"nome": nome, "idade": idade, "email": email}
            print("Usuário alterado com sucesso!\n")
        else:
            print("Usuário não encontrado.\n")
    except ValueError:
        print("Entrada inválida. Tente novamente.\n")

def excluir_usuario():
    listar_usuarios()
    try:
        indice = int(input("Digite o número do usuário que deseja excluir: "))
        if 0 <= indice < len(usuarios):
            confirmacao = input(f"Tem certeza que deseja excluir {usuarios[indice]['nome']}? (s/n): ")
            if confirmacao.lower() == 's':
                usuarios.pop(indice)
                print("Usuário excluído com sucesso!\n")
            else:
                print("Exclusão cancelada.\n")
        else:
            print("Usuário não encontrado.\n")
    except ValueError:
        print("Entrada inválida. Tente novamente.\n")

# Menu principal
def menu():
    while True:
        print("=== MENU ===")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Alterar usuário")
        print("4 - Excluir usuário")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            alterar_usuario()
        elif opcao == "4":
            excluir_usuario()
        elif opcao == "0":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executar o menu
menu()
