from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

miFrame = Frame(root)
miFrame.pack()

miFrame2 = Frame(root)
miFrame2.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollvert = Scrollbar(miFrame, command=textoComentario.yview)
scrollvert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollvert.set)

# ------------------------------------------------FUNCIÓN DE BOTONES-------------------------------------------------
def conexionBBDD():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))
            ''')

        messagebox.showinfo("BBDD", "BBDD Creada con éxito")

    except:
        messagebox.showwarning("Create", "Esa tabla ya existe")

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

    if valor=="yes":
        root.destroy()

def limpiarCampos():
    miNombre.set("")
    miId.set("")
    miApellido.set("")
    miDireccion.set("")
    miPass.set("")
    textoComentario.delete(1.0, END)

def crear():
    datos = miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), textoComentario.get("1.0", END)

    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", (datos))
    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro insertado con éxito")

def actualizar():
    datos = miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), textoComentario.get("1.0", END)

    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? " +
      "WHERE ID=" + miId.get(), (datos))

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro actualizado con éxito")
# ------------------------------------------------------INICIO----------------------------------------------------------


bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar")

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# ---------------------------------------------------CUADROS-----------------------------------------------------------



cuadroID=Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show='?')

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1)



# -------------------------------------------------------LABEL----------------------------------------------------------

idLabel= Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Password: ")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Dirección: ")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentario: ")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# --------------------------------------------------------BOTONES-------------------------------------------------------

botonCrear=Button(miFrame2, text="Create")
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Read")
botonCrear.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonCrear=Button(miFrame2, text="Update")
botonCrear.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonCrear=Button(miFrame2, text="Delete")
botonCrear.grid(row=1, column=3, sticky="e", padx=10, pady=10)

# ---------------------------------------------------FINAL LOOP---------------------------------------------------------

root.mainloop()