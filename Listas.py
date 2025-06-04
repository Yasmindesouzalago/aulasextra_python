#Aula 03

convidados= ["Beariz", "Lucas","Ana","Enzo","Valentina"]     
print("Primeiro covidado da festa:"+ convidados[-4])

#adicionar a lista substituindo 
convidados [-3] = "Letícia"
print (convidados [2])

#acrescentar no final da lista (append)
convidados.append("Joaquim")
print(convidados)

#Acrescenta na lista, na posição pedida (0)
convidados.insert(0,"Felipe")
print(convidados)
 
#remove, porem o computador se lembra depois 
convidadosRemovido= convidados.pop(1)
print(convidadosRemovido)

#remove, porem o computador não se lembra
del convidados[2]
print (convidados)

#usado para remover um item sem saber a posição dele, atribuindo a uma variavel( no caso nome) função em teste:(remove)
nome = input("Digite os clientes que estão de férias: ")
descansando = [descansando.strip() for descansando in nome.split(",")]

for cliente in descansando:
    if cliente in convidados:
        convidados.remove(cliente)

print(convidados)
print(f"Clientes de férias do mês: {descansando}")

#lista organizada de forma alfabetica(mudando no código)
convidados.sort()
print(convidados)

#Dps de listar aleatoriamente ele reverte 
convidados.sort(reverse=True)
print(convidados)

#organiza em ordem alfabetica apenas para o usúario
print(sorted(convidados))


