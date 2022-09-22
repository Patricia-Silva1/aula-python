soma=0

numerospares=[]
for i in range(1,7):
    num = int(input('Digite um número: '))
    if(num%2==0):
        numerospares.append(num)
        soma+=num
print(f'A soma dos números pares digitados é de {soma}')
