numsecret = int(input('Digite um número: '))
numpalpite = int(input(' Digite um número palpite: '))
while(numsecret!=numpalpite):
    if(numpalpite>numsecret):
        print('Esse número é maior que o numero secreto! ')
        numpalpite = int(input(' Digite um número palpite: '))
    elif(numpalpite<numsecret):
        print(' Esse número é menor do que o número secreto!')
        numpalpite = int(input(' Digite um número palpite: '))
else:
    print(' Parabéns, você descobriu o número secreto!')