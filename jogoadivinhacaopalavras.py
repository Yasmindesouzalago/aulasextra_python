## importa uma biblioteca para usarmos
import random

## função
def jogo_adivinhacao() :
    print(" Bem vindo ao jogo de adivinhação de palavres ")
    print(" você receberá dicas para adivinhar a palavra secreta ")

    palavras_e_dicas = {
    "pizza": "Um prato italiano popular, geralmente coberto com queijo, molho de tomate e diversos toppings.",
    "hambúrguer": "Um sanduíche composto por um pão cortado ao meio, recheado com carne moída e acompanhamentos.",
    "sushi": "Prato japonês que consiste em arroz temperado combinado com frutos do mar, vegetais e algas.",
    "taco": "Um prato mexicano composto por uma tortilla recheada com carne, queijo, alface, tomate e outros ingredientes.",
    "sorvete": "Uma sobremesa congelada feita de leite, creme e sabores variados, como chocolate e baunilha.",
    "salada": "Um prato frio feito de legumes, verduras e outros ingredientes, normalmente temperado com azeite ou molho.",
    "pasta": "Prato italiano à base de macarrão, geralmente servido com molho de tomate, carne ou vegetais.",
    "curry": "Prato indiano feito com uma mistura de especiarias, carne ou vegetais e um molho espesso.",
    "panqueca": "Um prato feito de massa frita na chapa, que pode ser servida doce ou salgada, com recheios variados.",
    "frango Frito": "Prato de frango empanado e frito até ficar crocante, geralmente servido com molhos."
}
    
    palavra_secreta, dica = random.choice(list(palavras_e_dicas.items()))
    tentativas_restantes = 5

    while tentativas_restantes > 0:
        print(f"Dica{dica}")
        print(f"Tentativas restantes: {tentativas_restantes}")
        resposta = input (" Consegue adivinhar a palavra secreta? ").lower()

        if resposta == palavra_secreta: 
           print("\n Parabenss, você conseguiu mesmo ", palavra_secreta)
           break
        else:
            tentativas_restantes -= 1
            print(" você errou. Mas, uma hora da certo")

    if tentativas_restantes == 0 :
            print("Quanta burice, a palavra era:", palavra_secreta)   

jogo_adivinhacao()

 



        







   

