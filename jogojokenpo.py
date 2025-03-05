import random

def pedra_papel_tesoura ():
    print("Bem vindo ao jogo de pedra papel e tesoura")
    print("Você jogara com o computador. vamos lá \n")
    
    opcoes = ["pedra", "papel", "tesoura"]
    pontos_jogador = 0
    pontos_computador = 0
    rodadas = 5

    for rodada in range(1, rodadas + 1):
        print(f"Rodada {rodada} de {rodada}")


    while True:
        print( "Escolha uma opção: Pedra, papel ou tesoura")
        escolha_jogador = input ("sua escolha"). lower()

        if escolha_jogador in opcoes:
            break
        else: 
            print( " escolha inválida, tente novamente. \n")

            escolha_computador = random.choice(opcoes)
            print(f" o computador escolheu:{ escolha_computador}")

        if escolha_computador == escolha_jogador:
            print ("empate!")

        elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
             (escolha_jogador == "papel" and escolha_computador == "pedra") or \
             (escolha_jogador == "tesoura" and escolha_computador == "papel"):
            print(" você ganhou")
            pontos_jogador += 1
                 
        else:
             print( " o computador ganhou essa rodada \n")
             pontos_computador += 1

    print("FIM DO JOGO")
    print(f"Placar fina: você {pontos_jogador} x {pontos_computador} computador")

    if pontos_jogador > pontos_computador:
        print("parabens, voce ganhou")

    elif pontos_jogador < pontos_computador:
        print("o computador venceu o jogo")

    else:
        print ("o jogo terminou em empate")

pedra_papel_tesoura()





        
                
            



