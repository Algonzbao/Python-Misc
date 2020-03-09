from tkinter import *
root = Tk()
root.config(bg="blue")
miFrame = Frame(root, width=1200, height=600)
miFrame.config(bg = "blue")
miFrame.pack()


nombreLabel = Label(miFrame, text = "NOMBRE")
nombreLabel.config(bg="blue")
nombreLabel.grid(row= 0, column=0)
cuadroTexto = Entry(miFrame)
cuadroTexto.config(bg="yellow")
cuadroTexto.grid(row =0, column = 1)


nombreLabel2 = Label(miFrame, text = "APELLIDO")
nombreLabel2.config(bg="blue")
nombreLabel2.grid(row= 0, column=3)
cuadroTexto2 = Entry(miFrame)
cuadroTexto2.config(bg="yellow")
cuadroTexto2.grid(row =0, column = 4)

nombreLabel3 = Label(miFrame, text = "SEGUNDO APELLIDO PERSONA")
nombreLabel3.config(bg="blue")
nombreLabel3.grid(row= 0, column=5, sticky="e")
cuadroTexto3 = Entry(miFrame)
cuadroTexto3.config(bg="yellow")
cuadroTexto3.grid(row =0, column = 6, sticky="e")

#cuadro de texto grande
textoLargo = Text(miFrame, width = 16, height= 5)
textoLargo.grid(row =0, column = 7)
scrollVert = Scrollbar(miFrame, command = textoLargo.yview)
textoLargo.config(yscrollcommand = scrollVert.set)
scrollVert.grid(row =0, column = 8)
textoLargo.config(bg="orange")

#boton
minombre = StringVar()

def codigoboton():
    minombre.set("Hua")

boton = Button(root, text= "Enviar", command= codigoboton)


boton.config(bg="silver")
boton.pack()

root.mainloop()