# Operadores de comparação
10 == 10 # Igual
10 != 10 # Diferente
10 >= 10 # Maior ou igual
10 <= 10 # Menor ou igual
10 > 10 # Maior
10 < 10 # Menor

# Operadores Lógicos
x = 10
print(x!=10)and(x>2) # Nesse caso as duas condições tem que ser verdadeira para sair True
print(x<20)or(x>30) # E nesse se uma for verdadeira sai true

# Testando o conhecimento
idade = int(input("Digite sua idade: "))
scan = idade >= 18
print(f"Sua idade é: {idade}")
print(f"Você é maior de idade: {scan}")