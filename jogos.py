import  adivinhacao
import  forca

def escolha_jogo():
    print("digite qual jogo quer jogar: ")
    resp = int(input("1)adivinhação (2)forca"))

    if(resp==2):
        forca.jogar()
    elif(resp==1):
        adivinhacao.jogar()

if(__name__=="__main__"):
    escolha_jogo()