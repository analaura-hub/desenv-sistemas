# cie um sistema de gerenciamento de petshop.
#devera ter os campos: nome, raca,idade,sexo,nome_dono,telefone_dono.
# o nome do arquivo json deve ser "petshop.json"
#faça o crud completo
#ao terminar, demonstrar o exercicio para o professor 




import json

# Função para carregar os dados do arquivo JSON
def carregar_dados():
    try:
        with open("petshop.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []  # Se o arquivo não existir, retorna uma lista vazia

# Função para salvar os dados no arquivo JSON
def salvar_dados(pets):
    with open("petshop.json", "w") as arquivo:
        json.dump(pets, arquivo, indent=4)

# Função para adicionar um novo pet
def adicionar_pet():
    print("----- Adicionar Novo Pet -----")
    nome = input("Nome do pet: ")
    raca = input("Raça: ")
    idade = input("Idade: ")
    sexo = input("Sexo: ")
    nome_dono = input("Nome do dono: ")
    telefone_dono = input("Telefone do dono: ")

    pet = {
        "nome": nome,
        "raca": raca,
        "idade": idade,
        "sexo": sexo,
        "nome_dono": nome_dono,
        "telefone_dono": telefone_dono
    }

    pets = carregar_dados()
    pets.append(pet)
    salvar_dados(pets)
    print("Pet adicionado com sucesso!\n")

# Função para listar todos os pets
def listar_pets():
    pets = carregar_dados()
    if not pets:
        print("Nenhum pet cadastrado.\n")
        return
    
    print("----- Lista de Pets -----")
    for i, pet in enumerate(pets, start=1):
        print(f"\nPet {i}:")
        print(f"  Nome: {pet['nome']}")
        print(f"  Raça: {pet['raca']}")
        print(f"  Idade: {pet['idade']}")
        print(f"  Sexo: {pet['sexo']}")
        print(f"  Nome do dono: {pet['nome_dono']}")
        print(f"  Telefone do dono: {pet['telefone_dono']}")
    print()

# Função para atualizar os dados de um pet
def atualizar_pet():
    pets = carregar_dados()
    if not pets:
        print("Nenhum pet cadastrado para atualizar.\n")
        return
    
    listar_pets()
    try:
        indice = int(input("Digite o número do pet que deseja atualizar: ")) - 1
        if indice < 0 or indice >= len(pets):
            print("Número inválido.\n")
            return
    except ValueError:
        print("Digite um número válido.\n")
        return

    pet = pets[indice]
    print("Digite os novos dados (aperte Enter para manter o valor atual):")

    nome = input(f"Nome ({pet['nome']}): ") or pet['nome']
    raca = input(f"Raça ({pet['raca']}): ") or pet['raca']
    idade = input(f"Idade ({pet['idade']}): ") or pet['idade']
    sexo = input(f"Sexo ({pet['sexo']}): ") or pet['sexo']
    nome_dono = input(f"Nome do dono ({pet['nome_dono']}): ") or pet['nome_dono']
    telefone_dono = input(f"Telefone do dono ({pet['telefone_dono']}): ") or pet['telefone_dono']

    pets[indice] = {
        "nome": nome,
        "raca": raca,
        "idade": idade,
        "sexo": sexo,
        "nome_dono": nome_dono,
        "telefone_dono": telefone_dono
    }

    salvar_dados(pets)
    print("Pet atualizado com sucesso!\n")

# Função para deletar um pet
def deletar_pet():
    pets = carregar_dados()
    if not pets:
        print("Nenhum pet cadastrado para deletar.\n")
        return
    
    listar_pets()
    try:
        indice = int(input("Digite o número do pet que deseja deletar: ")) - 1
        if indice < 0 or indice >= len(pets):
            print("Número inválido.\n")
            return
    except ValueError:
        print("Digite um número válido.\n")
        return
    
    pet = pets.pop(indice)
    salvar_dados(pets)
    print(f"Pet '{pet['nome']}' deletado com sucesso!\n")

# Função principal para mostrar o menu e chamar as funções
def menu():
    while True:
        print("----- Sistema Petshop -----")
        print("1. Adicionar Pet")
        print("2. Listar Pets")
        print("3. Atualizar Pet")
        print("4. Deletar Pet")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_pet()
        elif escolha == "2":
            listar_pets()
        elif escolha == "3":
            atualizar_pet()
        elif escolha == "4":
            deletar_pet()
        elif escolha == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.\n")

# Rodar o programa
menu()
