indicedepoluicao = float(input(' Insira o índice de poluição: '))
if(indicedepoluicao<=0.05 and indicedepoluicao<=0.25):
    print(' Os indíces estão dentro do limite aceitável de poluição')
elif(indicedepoluicao>0.3 and indicedepoluicao<=0.25):
    print(' As indústrias do grupo 1 precisam parar suas atividades')
elif (indicedepoluicao<=0.4):
    print(' As Indústrias do grupo 1 e 2 são intimadas a parar suas atividades')
elif (indicedepoluicao>=0.5):
    print(' Todas as empresas devem parara suas atividades')