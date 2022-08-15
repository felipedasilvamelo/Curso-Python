import random

n1 = str(input('Opção1: '))
n2 = str(input('Opção2: '))
n3 = str(input('Opção3: '))
n4 = str(input('Opção4: '))
n5 = str(input('Opção5: '))
lista = [n1, n2, n3, n4, n5]
escolha = random.choice(lista)
print(f'A opçao escolhida pelo pc foi: {escolha}')