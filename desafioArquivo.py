arquivo=open ('num.txt','w')
valora= (input(' escolha um número:'))
arquivo.write(valora)
arquivo.close()


# Abre o arquivo em modo de leitura
with open("num.txt", "r") as arquivo:
    # Lê o conteúdo do arquivo e converte para float
    valor = float(arquivo.read().strip())

if 0 <= valor <25:
    print('intervalo [0,25]')
elif 25 <= valor <50:
    print('intervalo [25,50]')
elif 50 <= valor <75:
    print('intervalo[50,75]')
elif 75<= valor <=100:
    print('intervalo[75,100]')
else:
    print("fora de intervalo")
