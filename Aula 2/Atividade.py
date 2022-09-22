time1 = input("Informe o time1: ")
gols_time1 = int(input("Informe os gols do", + time1 + ": ")
time2 = input("Informe o time2: ")
gols_time1 = int(input("Informe os gols do", + time2 + ": ")

#processamebto
resultado = ''
if gols_time1 > gols_time2:
    resultado = "O time " + time1 + " venceu!"
elif gols_time1 > gols_time2:
    resultado = "O time " + time2 + " venceu!"
else:
    resultado = "A partida terminou empatada!"

#Saida
print(resultado)