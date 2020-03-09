class Coche():
    def __init__(self):
        self.largo = 3
        self.__alto = 2
        self.ruedas = 4
        self.enmarcha = False
        self.aceite = "bien"
        self.temp = 80

    def Arrancar(self, arrancar):
        if(self.enmarcha == False & arrancar):
            if(self.aceite == "bien" and self.temp < 150):
                self.enmarcha = True
            else:
                print("Los valores de Aceite o de temperatura no permiten un arranque seguro")
        else:
            self.enmarcha = False;
        return self.enmarcha
    def arrancamos(self):
        print("Pulsa A para arrancar el coche")
        entrada = input()
        while(entrada != "A"):
            print("Pulsa A para arrancar el coche")
            entrada = input()
        if(entrada == "A"):
            self.Arrancar(True)
miCoche = Coche()
miCoche.arrancamos()
print(miCoche.enmarcha)