def boas_vindas ():
    print("Agora é 8:53 horário de brasília")
boas_vindas() 

def boas_vindas (nomeDeUsuario):
    print("Bem_vindo(a)",nomeDeUsuario, "a cntrl+play")
boas_vindas("Yas")

def velocidade(distancia,tempo):
    print(distancia/tempo)
velocidade( 100, 5)

def menor(a,b):         
    if a<=b:
        return a
    else:
        return b

a=5
b=1 
print("O menor valor entra" ,a, "e" ,b,"é", menor(a,b)) 

