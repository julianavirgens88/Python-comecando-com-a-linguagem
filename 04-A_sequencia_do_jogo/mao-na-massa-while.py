numero = 15
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = int(input("Digite o seu número: "))
    print("Você digitou", chute_str)

    acertou = chute_str == numero
    maior = chute_str > numero 
    menor = chute_str < numero

    if(acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou, o seu chute é maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute é menor do que o número secreto.")    
    
    rodada = rodada + 1

print("GAME OVER!")