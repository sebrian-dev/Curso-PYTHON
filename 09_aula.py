# Tuplas são coleções ordenadas e imutáveis. Existem dois métodos para tuplas: count e index. Podemos criar tuplas com ()

tupla = (1, 2, 3, 4, 5)
type(tupla) #checa o tipo do objeto criado

tupla1 = 1, 2, 3, 4, 5
type(tupla1)

# Métodos em tuplas

# index() - Retorna o índice do elemento especificado.
# count() - Conta o número de vezes que o elemento aparece na tupla.

tupla2 = ('a', 'b', 'c', 'd')
print(f"Índice de 'a': {tupla2.index('a')}")
print(f"Índice de 'd': {tupla2.index('d')}")

tupla3 = ('a', 'z', 'z', 'z', 'w')
print(f"Existe essa Qtde de 'Z': {tupla3.count('z')}")

