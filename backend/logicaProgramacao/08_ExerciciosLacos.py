senha_correta = input("configure uma senha")
senha = input("digite sua senha")

while senha != senha_correta:
    print("senha invalida")
    senha = input("digite a senha correta")
print("senha correta")