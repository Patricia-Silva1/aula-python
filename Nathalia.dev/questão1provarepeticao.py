soma = 0
presenca = int(input('Insira a quantidade de aulas comparecidas: '))
for i in range(1,4):
    nota = float(input('Insira sua nota: '))
    soma += nota
    media = soma/3
if(media>=6 and presenca>=40):
    print(f'O aluno teve média {media} e compareceu a quantidade mínima de aulas')
elif(media>=6 and presenca<40):
        print(f' O aluno teve média {media} mas não compareceu a aulas suficientes, então foi reprovado')
elif(media<6):
        print(f'O aluno teve média {media} e foi reprovado')
