produtos = []
preços=[]
for i in range(1,4):
    produto = str(input(' Insira o nome do produto: '))
    produtos.append(produto)
    preço = float(input(' Insira o preço do produto: '))
    preços.append(preço)
    print(f'{produtos} e {preços}')