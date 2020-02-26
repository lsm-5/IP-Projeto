class Automovel:
    def __init__(self, data):
        self.nome = data['nome'] 
        self.ano = data['ano']
        self.cor = data['cor']
        self.km = data['km']
        self.motor = data['motor']