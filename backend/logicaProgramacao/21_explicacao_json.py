# {} -> chaves: definir um objeto -> ficha de cadastro 
#                                   pessoa -nome, cpf, tel
# [] -> colchete: definir uma lista 
# chave/ valor: chave descreve o valor
#               "telefone"      "4499999-9999"
# sempre vai importar o json


import json 
inventario = []
# lendo o arquivo
try:
    with open("loja.json", "r") as arquivo:
        inventario = json.load(arquivo)
except FileNotFoundError:
    print("arquivo nao encontrado")
    
try:
    nome = input("Digite o Nome Do Produto: ")
    quantidade = int(input("Digite a Quantidade: "))
    preco = float(input("Digite o Preço: "))

except ValueError:
    print("Digite o Valor Corretamente")
    
# montar o objeto 
novo_produto = {"nome": nome,
                "quantidade":quantidade,
                "preco": preco,
                "em_estoque": quantidade > 0 #expressao verdadeiro falso
                }

# escrever o objeto no arquivo
inventario.append (novo_produto)
with open ("loja.json", "w") as arquivo:
    json.dump(inventario, arquivo, indent =4)
    #indent -> formatar o arquivo json
print("produto cadastrado com sucesso")
