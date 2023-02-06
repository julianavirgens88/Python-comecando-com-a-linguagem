print("*********************************")
print("Bem vindo ao jogo de Adivinhacao!")
print("*********************************")

numero_secreto = 34

chute_do_usuario = int(input("Digite o seu número:")); # o input funciona para que receba uma mensagem para imprimir no console. Pedir algo que o usuário deva digitar.
                                                       # o int faz com que seja lido um número, pois o input vai ler sempre uma string.

print("Você digitou" , chute_do_usuario)

if (numero_secreto == chute_do_usuario):
    print("Você acertou!")
else:
    print("Você errou!")


