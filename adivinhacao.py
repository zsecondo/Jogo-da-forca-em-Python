import random
def jogar():
    print("*****************************8*****")
    print("bem vindo no jogo de adivinhação!")
    print("*****************************8*****")
    numero_secreto = random.randrange(1,101)
    total_de_tentativas= 0
    rodada = 1
    pontos = 100

    print("qual o nivel de dificuldade?\n")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Digite o nivel de dificuldade: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    elif (nivel == 3):
        total_de_tentativas = 5
    else:
        print("dificuldade invalida")


    for rodada in range(1,total_de_tentativas+1):
        print("tentavidas {} de {} : ".format(rodada,total_de_tentativas))
        chute=input ("Digite um numero entre 1 e 100: ")
        print("você digitou: ",chute)
        chute=int(chute)
        if(chute<1 or chute>100):
            print("você deve digitar um número entre 1 e 100!")
            continue

        acertou= numero_secreto==chute
        maior=chute>numero_secreto
        menor = chute<numero_secreto


        if(acertou):
            print ("você acertou! e vez {} pontos" .format(pontos))
            break
        else:
            if(maior):
                print("você erroou! seu chute foi maior")
            elif(menor):
                print("você errou! seu chute foi menor ")
            pontos_perdidos= abs(numero_secreto-chute)
            pontos = pontos-pontos_perdidos

if(__name__=="__main__"):
    jogar()