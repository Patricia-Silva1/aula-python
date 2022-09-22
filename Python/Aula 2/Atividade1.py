from operator import ge


nomes = []

for i in range(5):
    nome = input("Informe o nome: ")
    nomes.append(nome)

for i in range(len(nomes)):
    print(i, nomes[i])