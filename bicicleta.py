class Bicicleta:
    marca =None
    cor = None
    def __init__(self,veloc_atual, veloc_max, altura_cela, veloc_min) :
        self.veloc_atual = veloc_atual
        self.veloc_max = veloc_max
        self.altura_cela = altura_cela
        self.veloc_min = veloc_min

        def qual_marca(self, marca):
            self.marca = marca

        def qual_cor(slf, cor):
            self.cor = cor

        def bicicleta_parada(self, veloc_atual):
            self.veloc_atual = veloc_atual

        def aumenta_veloc(self, veloc_min):
            self.veloc_min = veloc_min


        def velocidade_maxima(self, veloc_max):
            self.veloc_max = veloc_max

bicicleta = Bicicleta(0, 80, 0, 5)

print("marca", bicicleta.marca)
print("cor", bicicleta.cor)
print("veloc_atual", bicicleta.veloc_atual)
print("veloc_min", bicicleta.veloc_min)
print("veloc_max", bicicleta.veloc_max)


bicicleta.marca("Houston")
bicicleta.cor("vermelha")
bicicleta.veloc_min("20")
bicicleta.veloc_max(120)


print("marca", bicicleta.marca)
print("cor", bicicleta.cor)
print("veloc_min", bicicleta.veloc_min)
print("veloc_max", bicicleta.veloc_max)


        