print("*********************************")
print("Bem vindo ao jogo de Adivinhacao!")
print("*********************************")

numero = 15
total_de_tentativas = 3
rodada = 1

for rodada in range(1, total_de_tentativas + 1): # Entendendo o for: >>> para variável em série de valores:...faça algo
    # continuação da explicação:>>> for rodada in range(1,10):

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = int(input("Digite o seu número: "))
    print("Você digitou ", chute_str)

    if(chute_str < 1 or chute_str > 100):
        print("Você deve digitar um número entre 1 e 100:")
        continue # o break, que acaba, encerra o laço; e o continue, que acaba, encerra a iteração, continuando para a próxima.
    
    acertou = chute_str == numero
    maior = chute_str > numero
    menor = chute_str < numero

    if (acertou):
        print("Você acertou!")
        break  #faz terminar o laço, caso o jogador acerte.
    else:
        if (maior):
            print("Você errou, o seu chute é maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute é menor do que o número secreto.")

    rodada = rodada + 1

print("GAME OVER!")

#É importante saber que o for não deve ter parênteses.
#Podemos testar e ver que só fizemos 2 tentativas. Isso porque, como foi falado anteriormente, o segundo parâmetro da função range não é inclusivo, no caso do nosso jogo, `range(1,3) irá gerar a série 1 e 2 somente. Logo vamos somar 1 ao total de tentativas dentro da função range