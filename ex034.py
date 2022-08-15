s = float(input('Qual o sálario do funcionario? R$'))
if s <= 1250:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 0.10)
print(f'Quem ganhava R${s:.2f} passa a ganhar R${novo:.2f} agora')