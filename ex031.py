d = int(input("Qual a distância da sua viagem? "))
print(f'Você está prestes acomeçar uma viagem de {d:.1f}km.')
p = d * 0.50 if d <= 200 else d * 0.45
print(f'E o preço da sua passagem será de R${p:.2f}')


'''if d > 200:
    print(f'E o preço da sua passagem será de R${(d*0.45):.2f}')
else:
    print(f'E o preço da sua passagem será de R${(d*0.50)}')'''



