import os
import math
from mode import calcu as hj

if os.path.exists("arquivo.txt"):
    os.remove("arquivo.text")
else:
    print("O arquivo não existe")

print(dir(math))
help(math.expm1)
#Esta função evita a perda de precisão envolvida na avaliação direta de exp(x)-1 para pequenos x.
help(math.exp)
#Retorne e elevado à potência de x.
print(dir(os))
help(os.renames)
print(dir(hj))
help(hj.soma)


