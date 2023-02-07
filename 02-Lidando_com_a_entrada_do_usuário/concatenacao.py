nome = "Nico"
sobrenome = "Steppat"
print(nome + sobrenome)

# A resposta correta é NicoSteppat.O caractere + aqui não tem o significado de somar e sim de concatenar.
# Estamos concatenando (juntando) duas strings!

# Repare também que não há espaço entre as palavras. 
# Para que haja, basta fazer assim:

nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome)

# Lembrando que a função print automaticamente aplica um separador entre os valores. 
# O separador é um espaço por padrão, mas pode ser reconfigurado pelo parâmetro sep:

nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome, sep="_")