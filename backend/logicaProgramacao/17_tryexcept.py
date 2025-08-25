#Quando você executa um código em Python, é bem comum encontrar erros: seja ao tentar abrir um arquivo que não existe ou ao fazer uma conta que não dá certo,
#como dividir um número por zero.
#Esses erros, chamados de exceções, podem interromper a execução do seu programa e mostrar mensagens confusas para o usuário.
#O bloco try except serve justamente para isso: capturar essas exceções e permitir que você trate os erros de forma personalizada,
#evitando que o programa pare de funcionar ou que o usuário veja mensagens técnicas que ele não vai entender.

#try:
    # código que pode gerar um erro
#except:
    # código a ser executado caso ocorra um erro

#EXEMPLO 1
def dividir_lista_por_numero(lista, divisor):
    resultados = []
    for numero in lista:
        try:
            resultados.append(numero / divisor)
        except ZeroDivisionError as error:
            resultados.append(f"Erro: Não é possível dividir por zero!")
    return resultados

# Lista de números
numeros = [10, 20, 30, 40, 50]

# Entrada do usuário
divisor = int(input("Digite um número para dividir a lista: "))

# Chamando a função
resultado = dividir_lista_por_numero(numeros, divisor)

print("Resultado:", resultado)


#EXEMPLO 2
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            return file.read()
    except FileNotFoundError as error:
        return f"Erro: Arquivo '{nome_arquivo}' não encontrado!"
    except Exception as e:
        return f"Erro desconhecido: {e}"

# Teste com nome de arquivo fornecido
nome_do_arquivo = 'arquivo_exemplo.txt'
conteudo = ler_arquivo(nome_do_arquivo)

print(conteudo)

#EXEMPLO 3
def somar_lista(lista):
    soma = 0
    for item in lista:
        try:
            soma += item
        except TypeError as error:
            print(f"Erro: Não é possível somar um item não numérico ({item})")
    return soma

# Lista com elementos numéricos e não numéricos
itens = [10, 20, 'a', 30, None, 40]

# Chamando a função
resultado = somar_lista(itens)

print("Soma total:", resultado)


