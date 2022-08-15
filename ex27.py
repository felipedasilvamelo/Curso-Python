n = str(input('Digite seu nome completo: ')).strip()#serve para eliminar os espaços que o usuario colcoa antes e depoois
nome = n.split()#coloca dentro de uma lista e separa tudo, como ele divide, da para achar pelos números da ordem.
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
#print('Seu primeiro nome é {}'.format(nome[0]))
print(f'Seu último nome é {nome[len(nome)-1]}')
#print('Seu último nome é {}'.format(nome[len(nome)-1]))

#Também poderia colocar tudo isso em um único print(), colocando as 3 aspas e pulando linhas
