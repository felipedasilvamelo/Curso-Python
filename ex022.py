nome = str(input('Digite seu nome completo: ')).strip()
print(f"""Analisando seu nome...
Seu nome em maiúsculas é {nome.upper()}
Seu nome em minúsculas é {nome.lower()}
Seu nome tem ao todo {len(nome)-nome.count(' ')} letras""")
#Seu primeiro nome tem {len(nome[1:7])} letras
#Seu primeiro nome tem {nome.find(' ')} letras""") forma alternativa e mais facil
separa = nome.split()
#print('Seu priemiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')
