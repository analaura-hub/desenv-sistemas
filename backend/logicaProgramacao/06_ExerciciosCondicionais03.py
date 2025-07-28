salario = float(input("digite seu salario: "))
salarioanual = salario * 12
print ("seu salario anual e: ", salarioanual)

if(salario >= 5000):
    imposto = 0.08 * salario

elif(salario < 5000):
    imposto = 0.05 * salario

print("seu imposto mensal e: ", imposto)