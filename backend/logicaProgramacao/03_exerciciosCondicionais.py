nota1 =int(input("digite sua nota: "))
nota2 =int(input("digite sua nota:"))
nota3 =int(input("digite sua nota:"))
nota4 =int(input("digite sua nota:"))

nota_final = (nota1 + nota2 + nota3 + nota4)/4
print("sua media final foi:", nota_final)

if (nota_final >=80):
    print("exelente.")
elif (nota_final <80 and nota_final >=60):
    print("passou.")
elif (nota_final<60):
    print("ate ano que vem.") 
  
