quilometragem = float(input(' Insira a quilometragem: '))
if(quilometragem<250):
    print(f' a passagem fica no valor de {quilometragem*0.85:.2f}')
else:
    print(f' A passagem fica de {quilometragem*0.65:.2f}')