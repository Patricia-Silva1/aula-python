sair = 2


while True:
    if sair == 2:
        num1 = int(input('Digite 5um número: '))
        num2 = int(input(' Digite um segundo número: '))
        operação = int(input(' Escolha a operação: 1 - soma; 2 - subtração; 3 - multiplicação; 4 - Divisão '))

        if(operação==1):
            soma = num1+num2
            print(f'{num1} + {num2} = {soma} ')
            sair = int(input(' Quer sair do programa? 1 - sim; 2 - não!'))
                
        elif(operação==2):
            subtração = num1 - num2
            print(f'{num1} - {num2} = {subtração}')
            sair = int(input(' Quer sair do programa? 1 - sim; 2 - não!'))
                
        elif(operação==3):
            multiplicação = num1*num2
            print(f'{num1} X {num2} = {multiplicação} ')
            sair = int(input(' Quer sair do programa? 1 - sim; 2 - não!'))
            
        elif (operação==4):
            divisão = num1 / num2
            print(f'{num1} / {num2} = {divisão} ')
            sair = int(input(' Quer sair do programa? 1 - sim; 2 - não!'))
            
        elif (operação!=1 or operação!=2 or operação!=3 or operação!=4):
            print(' Opção inválida, tente novamente!')
    elif sair == 1:
        print('Até a proxima')
        break

    else:
        print('Valor inserido não corresponde ao pedido, favor insira 1 ou 2!')