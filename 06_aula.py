lista1 = [10, 20, 30, 40]
print(lista1)
print(type(lista1))

# Acessando valor pelo índice
lista2 = ['A', 'B', 'C']
print(lista2[0])

# Modificando um elemento de uma lista
lista2[0] = 'Z'
print(lista2)

# Indexação negativa, no caso seria de tras pra frente
b = ['a', 'b', 'c', 'd']
print(b[-1])

# Máx, mín, soma e tamanho
num = [31, 900, 546, 140, 15]
print(max(num))
print(min(num))
print(len(num))
print(sum(num))
media = sum(num)/len(num)
print(media)

print(f"Valor máx: {max(num)}")
print(f"Valor min: {min(num)}")
print(f"Tamanho da lista é: {len(num)}")
print(f"A soma dos elementos é: {sum(num)}")
print(f"Valor da média: {media}")