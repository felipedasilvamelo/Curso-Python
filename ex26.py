frase = str(input('Digite uma frase: ')).upper().strip()
'''print(f'A letra A aparece {frase.count("A")}')
#print('A letra A aparece {}'.format(frase.count('A')))
print(f'A primeira letra A apareceu na posção {frase.find("A")+1}')
#print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print(f'A última letra A apareceu na posição {frase.rfind("A")+1}')
#print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))'''
print(f'''A letra A aparece {frase.count("A")}
A primeira letra A apareceu na posição {frase.find("A")+1}
A última letra A apareceu na posição {frase.rfind("A")+1}''')

#sempre vai existir varias formas de fazer o código e reduzir eles a menos caracteres.