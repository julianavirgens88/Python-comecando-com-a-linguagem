contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 3

# Imprime:
# 1
# 4
# 7
# 10

# Para tranformar para for: 
for contador in range(1,11,3):
    print(contador)   

# A função range possui os seguintes parâmetros:

#range(start, stop, [step])
#Onde o step é opcional. Como queremos "pular" de 3 em 3, começando com 1 (start) até 10 (stop), podemos escrever:

for contador in range(1,11,3):
    print(contador)     