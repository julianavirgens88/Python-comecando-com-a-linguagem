import random #random precisa ser importado, conferir na biblioteca.

print("*********************************")
print("Bem vindo ao jogo de Adivinhacao!")
print("*********************************")

numero_secreto = random.randrange(1,11) #Forma de sortei de números inteiros entre 1 e 10.
total_de_tentativas = 3
rodada = 1

for rodada in range(1, total_de_tentativas + 1): # Entendendo o for: >>> para variável em série de valores:...faça algo
    # continuação da explicação:>>> for rodada in range(1,10):

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
        print("Você acertou!")
        break 
    else:
        if (maior):
            print("Você errou, o seu chute é maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute é menor do que o número secreto.")

    rodada = rodada + 1

print("GAME OVER!")
