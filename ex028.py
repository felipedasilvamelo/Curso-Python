from random import randint
from time import sleep # esse sleep faz ele esperar
computador = randint(0, 5)# Faz o computador "PENSAR"
print('\033[1;33m-=-' * 20)
print('Vou pensar em um número de 0 e 5. Tente adivinhar...\033[m')
print('\033[1;33m-=-\033[m' * 20)
jogador = int(input('Em que número eu pensei? '))# jogador tenta advinhar
print('\033[34mPROCESSANDO...\033[m')
sleep(2)
if jogador == computador:
    print('\033[32mPARABÉNS!\033[m Você conseguiu me vencer!')
else:
    print('\033[31mGANHEI!\033[m Eu pensei no número {} e não no {}!'.format(computador, jogador))
