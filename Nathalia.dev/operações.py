num = int(input(' Digite um número: '))
soma=0
multi=0
div=0
sub=0
num2=[1,2,3,4,5,6,7,8,9,10]

for i in num2:
    soma = num + i
    sub = num- i
    div = num/i
    multi = num*i
    print(f' {num} + {i} = {soma}')

    print(f'{num} - {i} = {sub}')
    
    print(f'{num} / {i} = {div}')
    
    print(f'{num} * {i} = {multi}')