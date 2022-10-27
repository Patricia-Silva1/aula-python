class Carro:
    def __init__(self, marca, modelo, ano, automatico):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.automatico = automatico
        self.velocidade = 0
        self.ligado = False
        self.VELOCIDADE_MAXIMA = 120
        
    def Ligar(self):
        self.ligado = True
        self.velocidade = 0
    
    def Desligar(self):
        self.ligado = False
        self.velocidade = 0
    
    def Acelerar(self):
        if self.ligado:
            self.velocidade += 10
            if self.velocidade > self.VELOCIDADE_MAXIMA: 
               self.velocidade = self.VELOCIDADE_MAXIMA
            
    def VerificarMarcha(self):
        if self.velocidade <= 20: return "1ª Marcha"
        elif self.velocidade <= 30: return "2ª Marcha"
        elif self.velocidade <= 40: return "3ª Marcha"
        elif self.velocidade <= 50: return "4ª Marcha"
        else: return "5ª Marcha"
        
        
        
        