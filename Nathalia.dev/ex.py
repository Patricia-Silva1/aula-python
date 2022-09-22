soma = 0
idades = []
nomes =[]

for i in range(1,4):
    nomes.append(str(input('Digite seu nome: ')))
    idades.append(int(input(' Digite sua idade: ')))

media = sum(idades) / len(idades)
print(f'A média das idades equivale a {media}')

for i in range(1):
    if(idades[0] < 20):
        print(f'{nomes[0]} ')
    elif(idades[1] < 20):
        print(f'{nomes[1]}')
    else:
        print(f'{nomes[2]}')

    if (idades[0] > idades[1] and idades[0] > idades[2]):
        print(f'{nomes[0]} é o mais velho com {idades[0]} de idade')

    elif (idades[1] > idades[0] and idades[1] > idades[2]):
        print(f'{nomes[1]} é o mais velho com {idades[1]} de idade')

    else:
        print(f'{nomes[2]} é o mais velho com {idades[2]} de idade')


