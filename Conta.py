class Conta:
    def __init__(self, agencia, numero = None):
        self.agencia = agencia
        if not numero:
            self.numero = self.GerarNumeroConta()
        else:
            self.numero = numero

    def ToString(self):
        return 'Ag: ' + self.agencia + '\nCC:' + self.numero
    
    def GerarNumeroConta(self):
        return '456789'