import random 

def jogar(): #função definida para ser executada quando chamada no arquivo jogos.py.
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhacao!")
    print("*********************************")

    numero_secreto = random.randrange(1,11) 
    total_de_tentativas = 3
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível:"))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10 
    else:
        total_de_tentativas = 5       

    for rodada in range(1, total_de_tentativas + 1): 

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = int(input("Digite o seu número: "))
        print("Você digitou ", chute_str)

        if(chute_str < 1 or chute_str > 100):
            print("Você deve digitar um número entre 1 e 100:")
            continue 
    
        acertou = chute_str == numero_secreto
        maior = chute_str > numero_secreto
        menor = chute_str < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break 
        else:
            if (maior):
                print("Você errou, o seu chute é maior do que o número secreto.")
        
            elif(menor):
                print("Você errou! O seu chute é menor do que o número secreto.")
        
            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
        
            pontos_perdidos = abs(numero_secreto - chute_str) 
            pontos = pontos - pontos_perdidos    

        rodada = rodada + 1

    print("GAME OVER!")

if(__name__ == "__main__"):
    jogar()    