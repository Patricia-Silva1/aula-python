qtd = int(input(' Insira a quantidade de vezes que quer repetir a pergunta: '))
for i in range(1,qtd+1):
    num = int(input(' Insira um número: '))
    if(num>=0):
        print(f'{num} é positivo!')
    else:
        print(f'{num} é negativo')