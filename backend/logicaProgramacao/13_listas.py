# crie uma lista de tarefas
# adicione 5 tarefas na lista
# adicioneuma tarefa na posiçao 2 da lista
# remova a tarefa "lavar louça" da lista 
# remover a tarefa da posiçao 1 da  lista

tarefas = []
tarefas.append("lavar louça")
tarefas.append("lavar banheiro")
tarefas.append("lavar quarto")
tarefas.append("varrer o chao")
tarefas.append("lavar quintal")

print(tarefas)

tarefas.insert(2, "lavar cachorro")

print(tarefas)

tarefas.remove("lavar louça")

print(tarefas)

tarefas.pop(1)

print(tarefas)