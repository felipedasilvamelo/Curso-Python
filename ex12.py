p = float(input('Qual é preço do produto? R$ '))
print(f'O produto que custava R${p:.2f}, na promoção com desconto de 5% vai custar R${(p-(p*(5/100))):.2f}')