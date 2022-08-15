#from math import hypot

import math

n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
#hi = (n1**2 + n2**2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hi))
'''hip = (n1**2 + n2**2)
hip2 = math.sqrt(hip)
print(f'A hipotenusa  vai medir {(hip2):.2f}')'''
#hi = hypot(n1, n2)
hi = math.hypot(n1, n2)
print('A hipotenusa vai medir {:.2f}'.format(hi))