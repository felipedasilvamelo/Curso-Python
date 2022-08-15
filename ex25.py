nome = str(input('Qual é o seu nome? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
#esse "in nome.upper()" serve para que independente que o usuario digite apareça "true" se tiver Silva
