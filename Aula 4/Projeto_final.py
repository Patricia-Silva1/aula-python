Clientes = []
Cliente = ""
TelefoneClientes = []
TelefoneCliente = ""

while(Cliente != "Fim"):
    Cliente = input("Informe nome do Cliente: (Digite 'Fim' finalizar programa)")
    Clientes.append(Cliente)
    TelefoneCliente = input("Informe telefone do Cliente: (Digite 'Fim' finalizar programa)")
    TelefoneClientes.append(TelefoneCliente)


import random

indice = random.randrange(0, len(Clientes))
print(Clientes[indice], TelefoneClientes[indice])



