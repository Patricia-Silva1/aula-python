

from operator import invert


notas = int(input("Informe quantidade de notas do aluno: "))
somanotas = 0

for notas in range(notas):
    notas = float(input("informe nota do aluno: "))
    somanotas += notas


print("media nota aluno", somanotas/notas)

invert = "dev"
