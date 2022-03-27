class Relogio:
    marca = None
    alimentação = None
    def __init__(self, estado, hora, minutos):
        self.estado = 'parado'
        self.hora = hora
        self.minutos = minutos

    def mudar_marca(self, marca):
        self.marca = marca

    def qual_alimentação(self, alimentação):
        self.alimentação = alimentação

    def mudar_estado(self, estado):
        self.estado = estado

    def que_hora(self, hora):
        self.hora +=hora
        
    def quantos_minutos(self, minutos):
        self.minutos+=minutos

relogio = Relogio('parado', 00, 00)
#Omitindo a chamada dos métodos...
print("marca", relogio.marca)
print("alimentaçaõ", relogio.alimentação)
print("estado", relogio.estado)
print("hora", relogio.hora)
print("minutos", relogio.minutos)

print('------------------------------------------------------------------')
#com atributos
relogio.mudar_estado("ligado")
relogio.que_hora(13)
relogio.quantos_minutos(20)
relogio.mudar_marca("Rolex")
relogio.qual_alimentação("Bateria")

print("marca", relogio.marca)
print("alimentaçaõ", relogio.alimentação)
print("mudar_estado {}".format( relogio.estado))
print("que_hora", relogio.hora)
print("quantos_minutos", relogio.minutos)
