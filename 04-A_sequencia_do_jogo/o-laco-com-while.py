print("*********************************")
print("Bem vindo ao jogo de Adivinhacao!")
print("*********************************")

numero_secreto = 34

total_de_tentativas = 3

rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa", rodada, "de", total_de_tentativas)
    chute_do_usuario = int(input("Digite o seu número:")) 
    print("Você digitou" , chute_do_usuario)

acertou = numero_secreto == chute_do_usuario
maior = chute_do_usuario > numero_secreto
menor = chute_do_usuario < numero_secreto 

if (acertou):
    print("Parabéns, você acertou!")
else:    
    if (maior):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    
    elif(menor):
        print("Você errou! O seu chute foi menor do que o número secreto.")

rodada = rodada + 1

print("FIM!")