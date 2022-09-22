time1 = str(input('Insira o nome do time: '))
time2 = str(input('Insira o nome do segundo time: '))
goals1 = int(input(f'Insira a quantidade de goals que o {time1} fez: '))
goals2 = int(input(f'Insira a quantidade de goals que o {time2} fez: '))

if(goals1 > goals2):
    print(f'O {time1} foi o vencedor ')
elif( goals2 > goals1):
    print(f' O time {time2} foi o vencedor')
else:
    print('O jogo terminou empatado')
