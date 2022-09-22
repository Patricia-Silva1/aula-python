for i in range(1,5):
    nome = str(input('Insira o nome do hospital: '))
    qtdrespiradores = int(input('Insira a quantidade de respiradores:'))
    ocupacao = int(input(' Digite a porcentagem da ocupacao: '))
    if(qtdrespiradores<50 and ocupacao>60):
        print(f'Serão adicionados 5 respiradores no hospital {nome}')