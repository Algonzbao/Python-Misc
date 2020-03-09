from tkinter import *
calculadora = Tk()
miCalcu = Frame(calculadora, width=1200, height=600)
miCalcu.config(bg = "brown")
miCalcu.pack()

#Pantalla
boton0 = Button(miCalcu, text="0")
boton0.grid(row= 3, column=1)
boton1 = Button(miCalcu, text="1")
boton1.grid(row= 0, column=0)
boton2 = Button(miCalcu, text="2")
boton2.grid(row= 0, column=1)
boton3 = Button(miCalcu, text="3")
boton3.grid(row= 0, column=2)
boton4 = Button(miCalcu, text="4")
boton4.grid(row= 1, column=0)
boton5 = Button(miCalcu, text="5")
boton5.grid(row= 1, column=1)
boton6 = Button(miCalcu, text="6")
boton6.grid(row= 1, column=2)
boton7 = Button(miCalcu, text="7")
boton7.grid(row= 2, column=0)
boton8 = Button(miCalcu, text="8")
boton8.grid(row= 2, column=1)
boton9 = Button(miCalcu, text="9")
boton9.grid(row= 2, column=2)
botonm = Button(miCalcu, text="+")
botonm.grid(row= 3, column=0)
botonr = Button(miCalcu, text="-")
botonr.grid(row= 3, column=2)
botoni = Button(miCalcu, text="=")
botoni.grid(row= 0, column=4)

pantallasalida = Label(miCalcu, width = 5, height = 1)
pantallasalida.grid(row =  1, column = 4)
#funcion








miCalcu.mainloop()