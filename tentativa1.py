from optparse import OptionContainer
import random
print("Bem vindo ao sistema de sorteio")

clientes = [] 

def cadastrar_cliente(nome:str, telefone:float):
    clientes.extend( ((nome + '') * int(telefone)).split() ) 
    return

def sorteia_ganhador():
    random.shuffle(clientes)
    print(f'Lista de clientes embaralhada: {clientes}')
    return random.choice(clientes)


Opao = int(input("Cadastrar cliente?0 - Não     1 - SIM "))

while opcao == 1:
    cliente = input("Informe o nome do cliente: ")
    telefone = float(input("Informe o telefone do cliente: "))

    while len(telefone.strip()) == "":
        print("Informe o número do telefone")
        cliente = float(input("Informe o nome do cliente: "))




for name in ():
    print (name)


print ("Esses são os participantes deste torneio")

input ('Tecle enter para continuar...\n')



sorteado = random.

print ("\nVocê foi o grande campeão da nossa inauguração! PARABÉNS!")

print ("\nObrigado por participar deste sorteio de inauguração!")


print ("\n----- PROGRAM FINISH -----")
    
    


