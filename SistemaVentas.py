from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
##import time
##import os

##colorPrincipal = "DarkSlateGray4"
##colorSecundario = "#81ADA7"
##colorHover = "#81BDB5"
##colorTitulo = "6DA49C"
##colorEntry = "#93cfc7"
conexion = sqlite3.connect("baseDeDatos/basededatos.db")
##
##def conectar():
##    if(os.path.isfile("baseDeDatos/basededatos.db") == True):
##        global conexion
##        
##        conexion.row_factory = sqlite3.Row
##        ventanaLogin()
##    else:
##        ventanaError()

##def guardar(conexion,daos,nombreTabla,nombreCampos,valores,vaciarEntry):

def ventanaPrincipal():
    ventana = Tk()
    ventana.title("Sistema de Ventas")
    ventana.config(bg="DarkSlateGray4")
    
    ancho = ventana.winfo_screenwidth()
    largo = ventana.winfo_screenheight()
    x = (ancho // 2) - (1000//2)
    y = (largo // 2) - (600//2)
    
    ventana.geometry(f"{1000}x{600}+{x}+{y}")
    ventana.resizable(0,0)
    fondo = PhotoImage(file="imagenes/fondo.png")
    labelFondo = Label(ventana, image=fondo)
    labelFondo.place(x=200,y=0)
    

#FRAMES
    frameBotones = Frame(ventana,bg="DarkSlateGray4")
    frameBotones.place(x=0,y=0,width=200,height=600)
    
    frameClientes = Frame(ventana,bg="red")
    
    frameProveedores = Frame(ventana,bg="blue")
    
    frameArticulos = Frame(ventana,bg="black")
    
    frameVentas = Frame(ventana,bg="green")
    
    frameCompras = Frame(ventana,bg="pink")
    #FUNCION BOTONES
    def cerrarFrames():
        frameProveedores.place_forget()
        frameArticulos.place_forget()
        frameCompras.place_forget()
        frameVentas.place_forget()
        frameClientes.place_forget()
        
    def mostrarClientes(evento):
        cerrarFrames()
        frameClientes.place(x=250,y=0,width=700,height=600)
        
    def mostrarProveedores():
        cerrarFrames()
        frameProveedores.place(x=250,y=0,width=700,height=600)

    def mostrarArticulos(evento):
        cerrarFrames()
        frameArticulos.place(x=250,y=0,width=700,height=600)
        
    def mostrarVentas(evento):
        cerrarFrames()
        frameVentas.place(x=250,y=0,width=700,height=600)
        
    def mostrarCompras(evento):
        cerrarFrames()
        frameCompras.place(x=250,y=0,width=700,height=600)
    
#BOTONES
    botonCliente = Button(frameBotones,text="Clientes",font=("Calibri",15),width=15,height=2)
    botonCliente.grid(row=0,column=0,padx=20,pady=20)
    botonCliente.bind("<Button-1>",mostrarClientes)
    
    botonProveedores = Button(frameBotones,text="Proveedores",font=("Calibri",15),width=15,height=2,command=mostrarProveedores)
    botonProveedores.grid(row=1,column=0,padx=20,pady=20)

    botonArticulos = Button(frameBotones,text="Articulos",font=("Calibri",15),width=15,height=2)
    botonArticulos.grid(row=2,column=0,padx=20,pady=20)
    botonArticulos.bind("<Button-1>",mostrarArticulos)

    botonVentas = Button(frameBotones,text="Ventas",font=("Calibri",15),width=15,height=2)
    botonVentas.grid(row=3,column=0,padx=20,pady=20)
    botonVentas.bind("<Button-1>",mostrarVentas)
    
    botonCompras = Button(frameBotones,text="Compras",font=("Calibri",15),width=15,height=2)
    botonCompras.grid(row=4,column=0,padx=20,pady=20)
    botonCompras.bind("<Button-1>",mostrarCompras)











    
    ventana.mainloop()

    

ventanaPrincipal()

























