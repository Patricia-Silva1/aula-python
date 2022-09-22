from random import randint

numsecreto = randint(1,10)
tentativas = 0
numpalpite = int(input('Digite um número: '))

while (numsecreto != numpalpite):
    if(numpalpite > numsecreto):
        print('Esse número é maior que o número secreto! Tente novamente!')
        numpalpite = int(input('Digite um número: '))
    elif(numpalpite < numsecreto):
        print('Esse número é menor que o número secreto. Tente novamente!')
        numpalpite = int(input('Digite um número: '))
    tentativas += 1
    
print('Parabéns, você acertou o número secreto')
print(f'Foram necessárias {tentativas} tentativas')

#código limpo é essencial