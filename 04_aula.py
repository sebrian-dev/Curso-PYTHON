# Na string cada letra tem uma posição começando de 0, exemplo abaixo estou pegando a letra da posição 0
nome = "UserPython"
print(nome[0])

# Agr nesse exemplo estou pegando da posição 0 até a 3, porém a letra da posição 3 é exclusive, ou seja, ele não conta
print(nome[0:3])

# Nesse exemplo seria caso eu quero deixar apenas o inicio ou final, e tbm pegar a palavra inteira
print(nome[4:])
print(nome[:4])
print(nome[:])

# A função "len" mostra o quantidade/tamanho da palavra
print(len(nome))

# As funções "upper" e "lower"
apelido = "João"
print(apelido.upper())
print(apelido.lower())

# Nesse caso "strip" seria tirar os espaços
ling = "  Python  "
print(ling.strip())

# A função "title" seria colocar cada palavra com letra maiusculas no inicio
nomeCompleto = "      matheus sebrian de souza      "
print(nomeCompleto.title())

print(nomeCompleto.strip().title())

# Para saber o índice usa a função "index"
print(nomeCompleto.index('m'))


