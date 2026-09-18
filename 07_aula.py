tupla = (1, 2, 3, 4)
lista = list(tupla)

serie = list(range(2010, 2021))
print(serie)

# Convertendo uma string para lista
frase = 'Eu sou dev'
print(frase.split(sep = ' '))

# Definindo lista em termos variaveis
num1 = 12
num2 = 34
num3 = 45
lista2 = [num1, num2, num3]
print(lista2)

# Agr ao contrário
valores = [90, 89, 87, 86]
num4, num5, num6, num7 = valores
print(num4)
print(num5)
print(num6)
print(num7)

# Fatiar lista
z = [4, 6, 8, 9, 5, 11]
print(z)
print(z[1:4])
print(z[1:])
print(z[:3])

# Verificar sem o elemento está na lista porém em boolean
f = ['F', 'K', 'L', 'G']
print('F' in f)
print('F' not in f)