arquivo= open('teste.txt', 'w', encoding='utf-8')
arquivo.write("Este é um arquivo criado em python!\n")
arquivo.write("Segunda linha do conteúdo")
arquivo.close()

#white dispensa o trabalho manual, de fechar
with open('teste.txt','a') as arquivo:
    arquivo.write('\n slk num compensa')

with open('teste.txt', 'r', encoding='utf-8') as arquivo:
    conteudo=arquivo.read()
    print(conteudo)
    conteudo2= arquivo.read()
    print(conteudo2)
    #arquivo seek, le do zero, a primeira linha
    arquivo.seek(0)
    conteudo4=arquivo.read()
    print(conteudo4)
    arquivo.seek(0)
    conteudo3=arquivo.readlines()
    print(conteudo3)
    conteudo4=arquivo.readline()
    print(conteudo3)

    
