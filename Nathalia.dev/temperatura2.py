temperatura = float(input(' Insira a temperatura: '))
 
if (temperatura <= 37):
    print(' Temperatura normal')
elif( temperatura <= 37.8):
    print(' Febril')
elif (temperatura > 37.8 and temperatura <= 38.5):
    print('Febre leve')
elif (temperatura > 38.5 and temperatura <= 39.4):
    print('febre moderada ')
elif (temperatura > 39.5):
    print('Febre grave')