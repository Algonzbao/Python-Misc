from tkinter import *
from tkinter import messagebox
import sqlite3
root = Tk()

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
        messagebox.showinfo("BBDD", "BBDD creada con exito")
    except:
        messagebox.showinfo("!Atencion¡", "La BBDD ya existe")

def salirAplicacion():
    valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")

    if valor == "yes":
        root.destroy()

def limpiarCampos():
    miNombre.set("")
    miId.set("")
    miApellido.set("")
    miDireccion.set("")
    miPass.set("")
    cuadroComentario.delete(1.0, END)

def crear():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + miNombre.get()+"','"
                     + miApellido.get() +"','"+ miDireccion.get()+"','" + miPass.get()+ "','"
                     + cuadroComentario.get()+"')")

    miConexion.commit()
    messagebox.sowinfo("BBDD", "Registro insertado con exito")
def lee():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID= "+ id.get())
    elUsuario = miCursor.fetchall()
    for usuario in elUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        cuadroComentario.insert(1.0, usuario[5])
    miConexion.commit()
def actualizar():
    miConexion= sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    datos = miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),cuadroComentario.get()
    miCursor.execute("UPADATE DATOSUSUARIOS SET NOMBRE_USUARIO = ?, PASSWORD = ?, APELLIDO = ?, DIRECCION = ?, COMENTARIOS= ?" + "WHERE ID= " + miId.get(),(datos))
    miConexion.commit()
barraMenu = Menu(root)
miFrame = Frame(root)
miFrame.pack()
root.config(menu=barraMenu, width = 300, height = 300)

bbddMenu = Menu(miFrame, tearoff=0)
bbddMenu.add_command(label="Conectar", command = conexionBBDD)
bbddMenu.add_command(label="Salir", command= salirAplicacion)

borrarMenu = Menu(miFrame, tearoff=0)
borrarMenu.add_command(label="Borrar campos")

crudMenu = Menu(miFrame, tearoff=0)
crudMenu.add_command(label = "Crear")
crudMenu.add_command(label = "Leer")
crudMenu.add_command(label = "Actualizar")
crudMenu.add_command(label = "Borrar")

ayudaMenu = Menu(miFrame, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de")

barraMenu.add_cascade(label="BBDD", menu = bbddMenu)
barraMenu.add_cascade(label="Borrar", menu = borrarMenu)
barraMenu.add_cascade(label="CRUD", menu = crudMenu)
barraMenu.add_cascade(label="Ayuda", menu = ayudaMenu)

miId = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPass = StringVar()
miDireccion = StringVar();
cuadroComentario= StringVar();

 #este es el q sale solo
#cuadroId = Entry(miFrame, textvariable = id)
#cuadroId.grid(row=0, column=1, padx= 10, pady=10)



id = Label(miFrame, text = "ID")
id.grid(row= 0, column= 3)
cuadroId = Entry(miFrame,textvariable= miId)
cuadroId.grid(row =0, column = 4)


nombre = Label(miFrame, text = "Nombre")
nombre.grid(row= 1, column= 3)
cuadroNombre = Entry(miFrame,textvariable= miNombre)
cuadroNombre.grid(row =1, column = 4)

apellido = Label(miFrame, text = "Apellido")
apellido.grid(row= 2, column= 3)
cuadroApellido = Entry(miFrame,textvariable= miApellido)
cuadroApellido.grid(row =2, column = 4)

direccion = Label(miFrame, text = "Direccion")
direccion.grid(row= 3, column= 3)
cuadrodireccion = Entry(miFrame,textvariable= miDireccion)
cuadrodireccion.grid(row =3, column = 4)

comentario = Label(miFrame, text = "Comentario")
comentario.grid(row= 4, column= 3)
cuadroComentario = Entry(miFrame)
cuadroComentario.grid(row =4, column = 4, padx= 10, pady= 10)
#scrollVert= Scrollbar(miFrame, command=comentario.yview)
#scrollVert.grig(row=4, column=3, sticky="nsew")
#comentario.config(yscrollcommand=scrollVert.set)

miFrame2=Frame(root)
miFrame2.pack()

botonCrear= Button(miFrame2, text = "Create", command = crear)
botonCrear.grid(row=1, column = 0, sticky=  "e",padx = 10, pady = 10)

botonLeer= Button(miFrame2, text = "Read", command = lee)
botonLeer.grid(row=1, column = 1, sticky=  "e",padx = 10, pady = 10)

botonActu= Button(miFrame2, text = "Update", command = actualizar)
botonActu.grid(row=1, column = 2, sticky=  "e",padx = 10, pady = 10)

botonBorrar= Button(miFrame2, text = "Delete", command = limpiarCampos)
botonBorrar.grid(row=1, column = 3, sticky=  "e",padx = 10, pady = 10)
conexionBBDD()
root.mainloop()