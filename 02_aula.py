nome = "João" #string
idade = 18 #int
altura = 1.73 # float

print(nome)
print(idade)
print(altura)

# Estou identificando qual o tipo da variável
print(type(nome))
print(type(idade))
print(type(altura))

# Nesse caso a variável x sofreu uma Sobrescrita
x = 10
x = 10.5
print(x)

# Receber dados do Usuário - Recebendo através do input recebe em string 
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
peso = input("Digite seu peso: ")

print(f"Seu nome é: {nome}")
print(f"Sua idade é: {idade}")
print(f"Seu peso é: {peso}")

# Declarando múltiplos valores em uma única linha
x, y, z, w = 10, 20, 40, 50
print(x, y, z, w)

# Declarando um valor para múltiplas variáveis
x = y = z = 10
print(x, y, z)