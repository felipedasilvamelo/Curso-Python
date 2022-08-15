from math import trunc
'''trunc() serve para quebrar o numero e deixar inteiro
n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n} e a sua porção inteira é {trunc(n)}')'''

n = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(n, int(n)))