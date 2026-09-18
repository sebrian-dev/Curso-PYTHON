"""
Peça o nome completo do usuário. Depois mostre:
O nome todo em MAIÚSCULO
O nome todo em minúsculo
O nome com a primeira letra de cada palavra maiúscula
Quantas letras tem o nome (sem contar espaços extras)
A primeira e a última letra do nome
"""
nome = input("Digite seu nome completo: ")
nome_limpo = nome.strip().replace(" ", "")
nome_limpo1 = nome.strip()
print(f"Seu nome: {nome.upper()}")
print(f"Seu nome: {nome.lower()}")
print(f"Seu nome: {nome.title()}")
print(f"Quantidade de letras: {len(nome_limpo)}")
print(f"Primeira letra: {nome_limpo1[0]}")
print(f"Última letra: {nome_limpo1[-1]}")