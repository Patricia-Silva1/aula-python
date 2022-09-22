mov = str(input('Insira seu movimento: '))
mov2 = str(input('Insira seu movimento: '))
while (mov=='pedra' or mov=='tesoura' or mov=='papel' or mov2=='papel' or mov2=='pedra' or mov2=='tesoura'):
    if(mov=='pedra' and mov2=='papel' or mov=='papel' and mov2=='pedra'):
        print('Papel embrulha  pedra')
        mov = str(input('Insira seu movimento: '))
        mov2 = str(input('Insira seu movimento: '))
    elif(mov=='pedra' and mov2=='tesoura' or mov=='tesoura' and mov2=='pedra'):
        print('Pedra quebra tesoura')
        mov = str(input('Insira seu movimento: '))
        mov2 = str(input('Insira seu movimento: '))
    elif(mov=='pedra' and mov2=='pedra' ):
        print('Movimento inválido, tente novamente!')
        mov = str(input('Insira seu movimento: '))
        mov2 = str(input('Insira seu movimento: '))
    elif(mov=='papel' and mov2=='tesoura' or mov=='tesoura' and mov2=='papel'):
        print('Tesoura corta papel')
        mov = str(input('Insira seu movimento: '))
        mov2 = str(input('Insira seu movimento: '))
    if (mov=='papel' and mov2=='papel'):
        print('Movimento inválido, tente novamente!')
        mov = str(input('Insira seu movimento: '))
        mov2 = str(input('Insira seu movimento: '))
    if(mov=='tesoura' and mov2=='tesoura'):
        print('Movimento inválido, tente novamente!')
        mov = str(input('Insira seu movimento: '))
        mov2 = str(input('Insira seu movimento: '))














#papel+tesoura= tesoura corta papel
#papel+pedra = papel embrulha pedra
# papel + papel = tente novamente
#tesoura+papel = tesoura corta papel
#tesoura +pedra = pedra quebra tesoura
# tesoura +tesoura = tente novamente
#pedra+papel = papel embrulha pedra
#pedra+tesoura = pedra quebra tesoura
#pedra+pedra = tente novamente!





