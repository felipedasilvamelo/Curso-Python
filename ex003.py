n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
cor = {'red':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m', 'limpa':'\033[m'}

s = n1+n2

print(f'A soma entre \033[34m{n1}\033[m e \033[31m{n2}\033[m é igual a \033[32m{s}\033[m!')
