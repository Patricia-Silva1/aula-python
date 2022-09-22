import random

#entrada
numero = int(input())

numero_sorteado = random.randrange(1, 10)
print(numero_sorteado)

acertou = False
while not acertou:
    if numero == numero_sorteado:
        print("Acertou Sacana")
        acertou = True
    else:
        numero = int(input("Digite o numero novamente: "))
        print("Errado ! Digite o Numero")
    numero = int(input())


print("Fim de jogo")