class Coche():
    largo = 3
    ancho = 30
    ruedas = 4
    marcha = False
    def arrancar(self):
        self.marcha = True
micoche = Coche()
micoche.arrancar()
print(micoche.marcha)