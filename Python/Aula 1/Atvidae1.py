Numero1 = int(input("Digite o primeiro numero: "))
Numero2 = int(input("Digite o segundo numero: "))
SimbolosMatematico = input("Digite a operacoa (+ | - | * | /)")

def CalculoMatematicaBasica(Numero1, Numero2, SimbolosMatematicos):
    if SimbolosMatematico == "+":
        return Numero1+Numero2
    elif SimbolosMatematico == "-":
        return Numero1-Numero2
    elif SimbolosMatematico == "*":
        return Numero1*Numero2
    elif SimbolosMatematico == "/":
        return Numero1/Numero2

Resultado = CalculoMatematicaBasica(Numero1, Numero2, SimbolosMatematico)

print(Resultado)


