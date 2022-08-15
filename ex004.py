a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('\033[31mSó tem espaços?\033[m ', a.isspace())
print('\033[32mÉ um número?\033[m ', a.isnumeric())
print('\033[33mÉ alfabético?\033[m ', a.isalpha())
print('\033[34mÉ alphanumérico?\033[m ', a.isalnum())
print('\033[35mEstá em maisúsculas?\033[m ', a.isupper())
print('\033[36mEstá em minúsculas?\033[m ', a.islower())
print('\033[37mEstá capitalizada?\033[m ', a.istitle())


#Esse "a" é o objeto que vc declarou, então sempre vai ser o objeto.isALGUMA-COISA
#Se mudar o "a" para o "B" ou para qualquer outra coisa, o código não funciona.

