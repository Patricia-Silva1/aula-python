for i in range(1,21,1):
    nome = str(input('Insira seu nome: '))
    sexo = int(input('Insira 1 para feminino e 2 para masculino: '))
    idade = int(input(' Insira a sua idade: '))
if(sexo==2 and idade>21):
    print(f'{nome}, {idade}')