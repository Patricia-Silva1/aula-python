numeros = []

for i in range(10):
    numero = int(input("Informe o numero: "))
    numeros.append(numero)

#for i in range(len(numeros)):
for numero in numeros:
    if numero % 2 == 1:
        print(numero)