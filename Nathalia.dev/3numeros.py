todososnúmeros =[]

for i in range(1,4):
    num = int(input('Digite um número: '))
    todososnúmeros.append(num)
if(todososnúmeros[0]>todososnúmeros[1] and todososnúmeros[0]>todososnúmeros[2]):
    print(f'{todososnúmeros[0]} é o maior número dos 3 digitados')
if (todososnúmeros[1]>todososnúmeros[0]and todososnúmeros[1]>todososnúmeros[2]):
    print(f'{todososnúmeros[1]} é o maior dos 3 números')
else:
    print(f'{todososnúmeros[2]} é o maior dos 3 numeros')
    
