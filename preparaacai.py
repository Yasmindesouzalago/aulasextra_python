def prepara_acai(*ingredientes, tamanho= "pequeno"):
    
    if ingredientes:
        print("\n Preparando um açaí", tamanho, "com os seguintes ingredientes:")
        for ingrediente in ingredientes:
            print("-",ingrediente)
    
    else:
         print("\t \t(Aguardando pedidos:)")

prepara_acai("banana","granola")
prepara_acai("morango","kiwi","leite em pó", tamanho="grande")
prepara_acai("Morango", tamanho="pequeno")

prepara_acai()