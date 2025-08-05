# DESAFIO
# PEDIR NOME E SENHA AO USUARIO 
# MOSTRAR "BEM VINDO" QUANDO ACERTAR A SENHA E O NOME
# APOS, PEDIR P SALARIO DO USUARIO 
# MOSTRAR SÁLARIO ANUAL
# SE O SÁLARIO ANUAL FOR MAIOR QUE 100 MIL MOSTAR MENSAGEM "RICO"

senha_correta = input("configure uma senha")
senha = input("digite sua senha")
nome = input("digite seu nome")
salario = float(input("digite seu salario"))
while senha != senha_correta:
    print("senha incorreta")
    senha =input

print("bem vindo", nome)
salarioanual= salario *12
if(salarioanual > 100000):
    print("rico")
else:
    print("faz o L")