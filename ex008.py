m = float(input('Digite uma distância em metros: '))

#Lembrando que daria para fazer cada variavel separadamente e colocar apenas a letra dela. ex: km = m/1000...
print(f'A medida de {m}m, corresponde a:')
print(f'{(m/1000)}km\n{(m/100)}hm\n{(m/10)}dam\n{(m*10)}dm\n{(m*100)}cm\n{(m*1000)}mm')