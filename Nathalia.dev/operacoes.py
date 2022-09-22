sair = 2

while True:
    if (sair == 2):
        num1 = int (input(' Insira o numero:'))
        num2 = int(input(' Insira o número: '))
        operacoes = int (input('1 - soma; 2 - subtração; 3 - multiplicação; 4 - divisão: '))

        if (operacoes==1):
            soma = num1 + num2
            print(f'{num1} + {num2} = {soma}')
            sair = int(input('1 - sim; 2 - não: '))

        elif(operacoes==2):     
            subtracao = num1 - num2
            print(f'{num1} - {num2} = {subtracao}')
            sair = int(input('1 - sim; 2 - não: ')) 

        elif(operacoes==3):     
            multiplicacao = num1 * num2
            print(f'{num1} * {num2} = {multiplicacao}')
            sair = int(input('1 - sim; 2 - não: ')) 

        elif(operacoes==4):     
            divisao = num1 / num2
            print(f'{num1} / {num2} = {divisao}')
            sair = int(input('1 - sim; 2 - não: ')) 

        elif(operacoes!=1 or operacoes!=2 or operacoes!= 3 or operacoes!= 4):
            print(f'Opção inválida, tente novamente!')
    elif(sair==1):
        print('Até a próxima')
        break    
    else:
        print(' Valor inserido não corresponde ao pedido, favor insira 1 ou 2!')


     