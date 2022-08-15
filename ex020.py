from random import shuffle
#import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)#esse comando"Shuffle" serve para embaralhar.
print(f'A ordem de apresentação será:\n {lista}')
#print(lista)