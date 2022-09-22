codigo = int(input(' Digite o código do funcionário: '))
anonascimento = int(input(' Insira o ano de nascimento do funcionário: '))
anocomeco = int(input('Digite o ano de entrada na empresa: '))
tempodetrabalho = anocomeco - anonascimento
if(tempodetrabalho>=30):
    print('Está qualificado para requerer a aposentadoria ')
elif(anonascimento<=1957):
    print('Requerer Aposentadoria')
elif (anonascimento<=1957 and tempodetrabalho>=25):
    print(' Requerer aposentadoria')
else:
    print('Não requerer')
