dist = int(input("Informe a distancia percorrida: "))
tmp = int(input("Informe o tempo decorrido: "))

def VerificaMulta(distancia, tempo):
    resultado = distancia/tempo
    
    if resultado >= 100:
        return "Voce foi multado"
    else:
        return "Parabens"
#-----------------------------------
mensagem = VerificaMulta(dist, tmp)
print(mensagem) 
