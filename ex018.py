import math
'''from math import radians, sin, cos, tan

e usar apenas a formatação--> sin(radians(n1)'''

n1 = int(input('Digite um ângulo que você deseja: '))
sen = math.sin(math.radians(n1))#formatação tem que converter para radianos
cos = math.cos(math.radians(n1))
tag = math.tan(math.radians(n1))
#print('O angulo de {} tem o seno de {:.2f}'.format(n1, sen))--fazer da outra forma é mais rápido!
print(f'O ângulo de {n1:.1f} tem o SENO de {sen:.2f}')
print(f'O ângulo de {n1:.1f} tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {n1:.1f} tem a TANGENTE de {tag:.2f}')
