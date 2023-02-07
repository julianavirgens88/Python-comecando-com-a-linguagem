idade1 = 10
idade2 = "20"
print(idade1 + idade2)

# imprime = unsupported operand type(s) for +: 'int' and 'str'
#Isso acontece porque não podemos realizar uma operação de soma envolvendo uma string. Para resolvermos o problema, podemos apelar para a função int(), 
# que converte uma string que contém um número, em um número inteiro:

idade1 = 10
idade2 = int("20")
print(idade1 + idade2)