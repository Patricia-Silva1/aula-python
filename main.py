from Carro import Carro

carro = Carro('Fiat', 'Palio', 2007, False)

carro.Ligar()

carro.Acelerar()
carro.Acelerar()

print(carro.VerificarMarcha())
carro.Acelerar()
print(carro.VerificarMarcha())

carro.Desligar()

