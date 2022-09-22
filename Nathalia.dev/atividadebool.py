cancela = True
temperatura = int(input(' Insira a temperatura: '))
if (temperatura>37):
    cancela = True
    print(f' A cancela não pode ser aberta')
else:
    print(' A cancela pode ser aberta')