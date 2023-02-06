print("*********************************")
print("Bem vindo ao jogo de Adivinhacao!")
print("*********************************")

numero_secreto = 34

chute_do_usuario = int(input("Digite o seu número:")); 

print("Você digitou" , chute_do_usuario)

acertou = numero_secreto == chute_do_usuario
maior = chute_do_usuario > numero_secreto
menor = chute_do_usuario < numero_secreto 

if (acertou):
    print("Você acertou!")
else:    
    if (maior):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    
    elif(menor):
        print("Você errou! O seu chute foi menor do que o número secreto.")
    #Podemos notar que, se o chute não for igual, nem maior que o número secreto, obviamente ele será menor, então o último if não é necessário.
    #Mas para esses casos, podemos fazer um else com uma condição de entrada, o elif. Vamos utilizá-lo para deixar o código mais semântico, já que na prática não há diferença.
    
print("Fim do jogo!")