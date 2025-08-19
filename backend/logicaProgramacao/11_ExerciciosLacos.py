# 2 crie uma função que calcule o imposto anual do seu salario_ 22%
# 3 crie uma função que valide se a senha esta correta

# 1 crie uma função que faça a media de 3 valores
def media (num1,num2,num3):
    media = (num1 + num2 + num3) / 3
    print("media:", media)
media (3,2,1)

# 2 crie uma função que calcule o imposto anual do seu salario_ 22%

def imposto(salario):
    salarioanual = salario * 12
    print("seu salarioanual e:", salarioanual)

    if (salario >= 1000):
        imposto = 0.22 * salario
    elif (salario <= 7000):
        imposto = 0.22 * salario
    print ("seu imposto mensal e", imposto)
imposto (10000)