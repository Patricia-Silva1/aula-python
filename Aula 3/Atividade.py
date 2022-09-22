print("Informe o valor do custo fixo da tonelada:")
custo_fixo = float(input())

acumulador = 0
while True:
    mes = input("informe o mês corrente: ")
    if mes == "sair":
        break
    else:
        print("Informe o total de toneladas para o mês de", mes,":")
        total_ton = float(input())
        acumulador += total_ton

#mostrar resultado
print("o total acumulado do periodo foi:", acumulador * custo_fixo)