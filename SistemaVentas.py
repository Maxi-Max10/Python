from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import time

conexion = sqlite3.connect("baseDeDatos/basededatos1.db")
conexion.row_factory = sqlite3.Row

def ventanaPrincipal():
    ventana = Tk()
    ventana.title("Sistema de Ventas")
    ventana.config(bg="DarkSlateGray4")
##    ventana.iconbitmap("imagenes/icono.ico")
    ancho = ventana.winfo_screenwidth()
    largo = ventana.winfo_screenheight()
    x = (ancho // 2) - (1000//2)
    y = (largo // 2) - (600//2)   
    ventana.geometry(f"{1000}x{600}+{x}+{y}")
    ventana.resizable(0,0)
    fondo = PhotoImage(file="imagenes/fondo.png")
    labelFondo = Label(ventana,image=fondo,bd=0,relief="flat")
    labelFondo.place(x=190,y=-20)




#FRAMES
    frameBotones = Frame(ventana,bg="DarkSlateGray4")
    frameBotones.place(x=0,y=0,width=200,height=600)
    ##CLIENTES
    frameClientes = Frame(ventana,bg="#56837D")    
    frameDetallesClientes = Frame(frameClientes,bg="#56837D")
    frameDetallesClientes.place(x=0,y=0,width=781,height=500)
    frameListarClientes = Frame(frameClientes,bg="#56837D")
    frameProveedor = Frame(ventana,bg="#56837D")    
    frameDetallesProveedor = Frame(frameProveedor,bg="#56837D")
    frameDetallesProveedor.place(x=0,y=0,width=781,height=500)
    frameListarProveedor = Frame(frameProveedor,bg="#56837D")
    frameArticulo = Frame(ventana,bg="#56837D")
    frameDetallesArticulo = Frame(frameArticulo,bg="#56837D")
    frameDetallesArticulo.place(x=0,y=0,width=781,height=500)
    frameListarArticulo = Frame(frameArticulo,bg="#56837D")




    frameBotonesClientes = Frame(frameClientes,bg="#56837D")
    frameBotonesClientes.place(x=0,y=500,width=800,height=100)
    frameBotonesProveedor = Frame(frameProveedor,bg="#56837D")
    frameBotonesProveedor.place(x=0,y=500,width=800,height=100)
    frameBotonesArticulo = Frame(frameArticulo,bg="#56837D")
    frameBotonesArticulo.place(x=0,y=500,width=800,height=100)

    frameBarraHerramienta = Frame(ventana,bg="gray")
    frameBarraHerramienta.place(x=0,y=570,height=30,width=1000)    
    labelHora = Label(frameBarraHerramienta,font=("Calibri",15),bg="gray",fg="white")
    labelHora.place(x=900,y=0)
    usuario = "Admin"
    labelUsuario = Label(frameBarraHerramienta,text="Bienvenido "+usuario,font=("Calibri",20),bg="gray",fg="white")
    labelUsuario.place(x=10,y=0)
    def reloj():
        global time1
        time1=""
        time2=time.strftime("%H:%M:%S")
        if(time1 != time2):
            labelHora.configure(text=time2)
            labelHora.after(500,reloj)
    reloj()
    def vacios(datos):
        for dato in datos:
            if(dato == ""):
                return False
        return True
    def soloLetras(datos):
        for letra in datos:
            if(ord(letra) != 32):
                if(letra.isalpha() == False): ##no es un espacio y no es una letra valida
                    return False            
        return True
    def soloNumeros(datos):
        for numero in datos:
            if(ord(numero) ==  46):
                if(numero.isdigit() == False):
                    return False
        return True
    
    def vaciarEntryCliente():
        entryIdCliente.config(state="normal")
        entryIdCliente.delete(0,END)
        entryIdCliente.config(state="readonly")
        entryRazonSocialCliente.delete(0,END)
        entryCuitCliente.delete(0,END)
        entryDireccionCliente.delete(0,END)
        entryLocalidadCliente.delete(0,END)
        entryProvinciaCliente.delete(0,END)
        entryCodigoPostalCliente.delete(0,END)
        entryTelefonoCliente.delete(0,END)
        entryIvaCliente.delete(0,END)
    def vaciarEntryProveedor():
        entryIdProveedor.config(state="normal")
        entryIdProveedor.delete(0,END)
        entryIdProveedor.config(state="readonly")
        entryRazonSocialProveedor.delete(0,END)
        entryCuitProveedor.delete(0,END)
        entryDireccionProveedor.delete(0,END)
        entryLocalidadProveedor.delete(0,END)
        entryProvinciaProveedor.delete(0,END)
        entryCodigoPostalProveedor.delete(0,END)
        entryTelefonoProveedor.delete(0,END)
        entryIvaProveedor.delete(0,END)
    def vaciarEntryArticulo():
        entryIdArticulo.config(state="normal")
        entryIdArticulo.delete(0,END)
        entryIdArticulo.config(state="readonly")
        entryCodigoArticulo.delete(0,END)
        entryMarcaArticulo.delete(0,END)
        entryModeloArticulo.delete(0,END)
        entryCategoriaArticulo.delete(0,END)
        entryStockArticulo.delete(0,END)
        entryPrecioCostoArticulo.delete(0,END)
        entryPrecioVentaArticulo.delete(0,END)
        
        
    def buscarCliente():
        datos = (entryBuscarCliente.get(),)
        if(vacios(datos)):            
            tabla = conexion.cursor()
            sql = "SELECT * FROM clientes WHERE razonSocialCliente = ?"
            tabla.execute(sql,datos)
            datosCliente = tabla.fetchall()
            if(len(datosCliente) > 0):
                if(len(datosCliente) > 1):
                   messagebox.showinfo("Sistema","Se han encotrado varias coincidencias")
                   vaciarEntryCliente()
                   comboBuscar.place(x=500,y=120)
                   labelComboBuscar.place(x=500,y=80)
                   listadoCiut = []
                   for dato in datosCliente:
                       listadoCiut.append(dato["cuitCliente"])
                   comboBuscar["values"] = listadoCiut
                   def mostrarEnEntry(evento):
                       vaciarEntryCliente()
                       cuit = comboBuscar.get()
                       for dato in datosCliente:
                           if(dato["cuitCliente"] == cuit):
                               entryIdCliente.config(state="normal")
                               entryIdCliente.insert(END,dato["idCliente"])
                               entryIdCliente.config(state="readonly")#vuleve todo blanco
                               entryRazonSocialCliente.insert(END,dato["razonSocialCliente"])
                               entryCuitCliente.insert(END,dato["cuitCliente"])
                               entryDireccionCliente.insert(END,dato["DireccionCliente"])
                               entryLocalidadCliente.insert(END,dato["localidadCliente"])
                               entryProvinciaCliente.insert(END,dato["provinciaCliente"])
                               entryCodigoPostalCliente.insert(END,dato["codigoPostalCliente"])
                               entryTelefonoCliente.insert(END,dato["telefonoCliente"])
                               entryIvaCliente.insert(END,dato["ivaCliente"])     
                   comboBuscar.bind("<<ComboboxSelected>>",mostrarEnEntry)
                else:
                    vaciarEntryCliente()
                    
                    for dato in datosCliente:
                       entryIdCliente.config(state="normal")
                       entryIdCliente.insert(END,dato["idCliente"])
                       entryIdCliente.config(state="readonly")
                       entryRazonSocialCliente.insert(END,dato["razonSocialCliente"])
                       entryCuitCliente.insert(END,dato["cuitCliente"])
                       entryDireccionCliente.insert(END,dato["DireccionCliente"])
                       entryLocalidadCliente.insert(END,dato["localidadCliente"])
                       entryProvinciaCliente.insert(END,dato["provinciaCliente"])
                       entryCodigoPostalCliente.insert(END,dato["codigoPostalCliente"])
                       entryTelefonoCliente.insert(END,dato["telefonoCliente"])
                       entryIvaCliente.insert(END,dato["ivaCliente"])
                       
            else:
                 vaciarEntryCliente()
                 messagebox.showwarning("Sistema","No se encontró")                
        else:
            messagebox.showwarning("Sistema","Ingrese algo a buscar")

    def buscarProveedor():
        datos = (entryBuscarProveedor.get(),)
        if(vacios(datos)):            
            tabla = conexion.cursor()
            sql = "SELECT * FROM proveedores WHERE razonSocialProveedor = ?"
            tabla.execute(sql,datos)
            datosProveedor = tabla.fetchall()
            if(len(datosProveedor) > 0):
                if(len(datosProveedor) > 1):
                   messagebox.showinfo("Sistema","Se han encotrado varias coincidencias")
                   vaciarEntryProveedor()
                   comboBuscar.place(x=500,y=120)
                   labelComboBuscar.place(x=500,y=80)
                   listadoCiut = []
                   for dato in datosCliente:
                       listadoCiut.append(dato["cuitProveedor"])
                   comboBuscar["values"] = listadoCiut
                   def mostrarEnEntry(evento):
                       vaciarEntryProveedores()
                       cuit = comboBuscar.get()
                       for dato in datosProveedor:
                           if(dato["cuitProveedor"] == cuit):
                               entryIdProveedor.config(state="normal")
                               entryIdProveedor.insert(END,dato["idProveedor"])
                               entryIdProveedor.config(state="readonly")#vuleve todo blanco
                               entryRazonSocialProveedor.insert(END,dato["razonSocialProveedor"])
                               entryCuitProveedor.insert(END,dato["cuitProveedor"])
                               entryDireccionProveedor.insert(END,dato["DireccionProveedor"])
                               entryLocalidadProveedor.insert(END,dato["localidadProveedor"])
                               entryProvinciaProveedor.insert(END,dato["provinciaProveedor"])
                               entryCodigoPostalProveedor.insert(END,dato["codigoPostalProveedor"])
                               entryTelefonoProveedor.insert(END,dato["telefonoProveedor"])
                               entryIvaProveedor.insert(END,dato["ivaProveedor"])     
                   comboBuscar.bind("<<ComboboxSelected>>",mostrarEnEntry)
                else:
                    vaciarEntryProveedor()
                    
                    for dato in datosProveedor:
                       entryIdProveedor.config(state="normal")
                       entryIdProveedor.insert(END,dato["idProveedor"])
                       entryIdProveedor.config(state="readonly")
                       entryRazonSocialProveedor.insert(END,dato["razonSocialProveedor"])
                       entryCuitProveedor.insert(END,dato["cuitProveedor"])
                       entryDireccionProveedor.insert(END,dato["DireccionProveedor"])
                       entryLocalidadProveedor.insert(END,dato["localidadProveedor"])
                       entryProvinciaProveedor.insert(END,dato["provinciaProveedor"])
                       entryCodigoPostalProveedor.insert(END,dato["codigoPostalProveedor"])
                       entryTelefonoProveedor.insert(END,dato["telefonoProveedor"])
                       entryIvaProveedor.insert(END,dato["ivaProveedor"])
                       
            else:
                 vaciarEntryProveedor()
                 messagebox.showwarning("Sistema","No se encontró")                
        else:
            messagebox.showwarning("Sistema","Ingrese algo a buscar")
    def buscarArticulo():
        datosA = (entryBuscarArticulo.get(),)
        if(vacios(datosA)):            
            tablaA = conexion.cursor()
            sqlA = "SELECT * FROM articulos WHERE codigoArticulo = ?"
            tabla.execute(sqlA,datosA)
            datosArticulo = tablaA.fetchall()
##            if(len(datosArticulo) > 0):
##                if(len(datosArticulo) > 1):
##                   messagebox.showinfo("Sistema","Se han encotrado varias coincidencias")
##                   vaciarEntryArticulo()
##                   comboBuscar.place(x=500,y=120)
##                   labelComboBuscar.place(x=500,y=80)
##                   listadoCiut = []
##                   for dato in datosCliente:
##                       listadoCiut.append(dato["cuitCliente"])
##                   comboBuscar["values"] = listadoCiut
##                   def mostrarEnEntry(evento):
##                       vaciarEntryCliente()
##                       cuit = comboBuscar.get()
##                       for dato in datosCliente:
##                           if(dato["cuitCliente"] == cuit):
##                               entryIdCliente.config(state="normal")
##                               entryIdCliente.insert(END,dato["idCliente"])
##                               entryIdCliente.config(state="readonly")#vuleve todo blanco
##                               entryRazonSocialCliente.insert(END,dato["razonSocialCliente"])
##                               entryCuitCliente.insert(END,dato["cuitCliente"])
##                               entryDireccionCliente.insert(END,dato["DireccionCliente"])
##                               entryLocalidadCliente.insert(END,dato["localidadCliente"])
##                               entryProvinciaCliente.insert(END,dato["provinciaCliente"])
##                               entryCodigoPostalCliente.insert(END,dato["codigoPostalCliente"])
##                               entryTelefonoCliente.insert(END,dato["telefonoCliente"])
##                               entryIvaCliente.insert(END,dato["ivaCliente"])     
##                   comboBuscar.bind("<<ComboboxSelected>>",mostrarEnEntry)
##                else:
##                    vaciarEntryCliente()
##                    
##                    for dato in datosCliente:
##                       entryIdCliente.config(state="normal")
##                       entryIdCliente.insert(END,dato["idCliente"])
##                       entryIdCliente.config(state="readonly")
##                       entryRazonSocialCliente.insert(END,dato["razonSocialCliente"])
##                       entryCuitCliente.insert(END,dato["cuitCliente"])
##                       entryDireccionCliente.insert(END,dato["DireccionCliente"])
##                       entryLocalidadCliente.insert(END,dato["localidadCliente"])
##                       entryProvinciaCliente.insert(END,dato["provinciaCliente"])
##                       entryCodigoPostalCliente.insert(END,dato["codigoPostalCliente"])
##                       entryTelefonoCliente.insert(END,dato["telefonoCliente"])
##                       entryIvaCliente.insert(END,dato["ivaCliente"])
##                       
##            else:
##                 vaciarEntryCliente()
##                 messagebox.showwarning("Sistema","No se encontró")                
        else:
            messagebox.showwarning("Sistema","Ingrese algo a buscar")
    
    labelComboBuscar = Label(frameDetallesClientes,text="Elija cliente",font=("Calibri",15),fg="white",bg="#56837D")        
    comboBuscar = ttk.Combobox(frameDetallesClientes,width=15,font=("Calibri",15))
    entryBuscarCliente = Entry(frameDetallesClientes,font=("Calibri",15),width=40)
    entryBuscarCliente.grid(row=0,column=0,columnspan=2,pady=(10,20),padx=(50,20))
    botonBuscarCliente = Button(frameDetallesClientes,text="Buscar",font=("Calibri",15),command=buscarCliente,width=10,height=1)
    botonBuscarCliente.grid(row=0,column=2,sticky=W,pady=(10,20))
    labelIdCliente = Label(frameDetallesClientes,text="ID",font=("Calibri",15),width=15)
    labelIdCliente.grid(row=1,column=0,pady=(0,20),padx=(30,20))
    entryIdCliente = Entry(frameDetallesClientes,font=("Calibri",15),width=25,state="readonly")
    entryIdCliente.grid(row=1,column=1,pady=(0,20),padx=(30,20))
    labelRazonSocialCliente = Label(frameDetallesClientes,text="Razón Social",font=("Calibri",15),width=15)
    labelRazonSocialCliente.grid(row=2,column=0,pady=(0,20),padx=(30,20))
    entryRazonSocialCliente = Entry(frameDetallesClientes,font=("Calibri",15),width=25)
    entryRazonSocialCliente.grid(row=2,column=1,pady=(0,20))  
    labelCuitCliente = Label(frameDetallesClientes,text="CUIT",font=("Calibri",15),width=15)
    labelCuitCliente.grid(row=8,column=0,pady=(0,20),padx=(30,20))
    entryCuitCliente = Entry(frameDetallesClientes,font=("Calibri",15),width=25)
    entryCuitCliente.grid(row=8,column=1,pady=(0,20))
    labelDireccionCliente = Label(frameDetallesClientes,text="Dirección",font=("Calibri",15),width=15)
    labelDireccionCliente.grid(row=3,column=0,pady=(0,20),padx=(30,20))
    entryDireccionCliente = Entry(frameDetallesClientes,font=("Calibri",15),width=25)
    entryDireccionCliente.grid(row=3,column=1,pady=(0,20))
    labelLocalidadCliente = Label(frameDetallesClientes,text="Localidad",font=("Calibri",15),width=15)
    labelLocalidadCliente.grid(row=4,column=0,pady=(0,20),padx=(30,20))
    entryLocalidadCliente = Entry(frameDetallesClientes,font=("Calibri",15),width=25)
    entryLocalidadCliente.grid(row=4,column=1,pady=(0,20))    
    labelProvinciaCliente = Label(frameDetallesClientes,text="Provincia",font=("Calibri",15),width=15)
    labelProvinciaCliente.grid(row=9,column=0,pady=(0,20),padx=(30,20))
    entryProvinciaCliente = Entry(frameDetallesClientes,font=("Calibri",15),width=25)
    entryProvinciaCliente.grid(row=9,column=1,pady=(0,20))
    labelCodigoPostalCliente = Label(frameDetallesClientes,text="Código Postal",font=("Calibri",15),width=15)
    labelCodigoPostalCliente.grid(row=5,column=0,pady=(0,20),padx=(30,20))
    entryCodigoPostalCliente = Entry(frameDetallesClientes,font=("Calibri",15),width=25)
    entryCodigoPostalCliente.grid(row=5,column=1,pady=(0,20))
    labelTelefonoCliente = Label(frameDetallesClientes,text="Teléfono",font=("Calibri",15),width=15)
    labelTelefonoCliente.grid(row=6,column=0,pady=(0,20),padx=(30,20))
    entryTelefonoCliente = Entry(frameDetallesClientes,font=("Calibri",15),width=25)
    entryTelefonoCliente.grid(row=6,column=1,pady=(0,20))
    labelIvaCliente = Label(frameDetallesClientes,text="IVA",font=("Calibri",15),width=15)
    labelIvaCliente.grid(row=7,column=0,pady=(0,20),padx=(30,20))
    entryIvaCliente = Entry(frameDetallesClientes,font=("Calibri",15),width=25)
    entryIvaCliente.grid(row=7,column=1,pady=(0,20))

    labelComboBuscar = Label(frameDetallesProveedor,text="Elija cliente",font=("Calibri",15),fg="white",bg="#56837D")        
    comboBuscar = ttk.Combobox(frameDetallesProveedor,width=15,font=("Calibri",15))
    entryBuscarProveedor = Entry(frameDetallesProveedor,font=("Calibri",15),width=40)
    entryBuscarProveedor.grid(row=0,column=0,columnspan=2,pady=(10,20),padx=(50,20))
    botonBuscarProveedor = Button(frameDetallesProveedor,text="Buscar",font=("Calibri",15),command=buscarProveedor,width=10,height=1)
    botonBuscarProveedor.grid(row=0,column=2,sticky=W,pady=(10,20))
    labelIdProveedor = Label(frameDetallesProveedor,text="ID",font=("Calibri",15),width=15)
    labelIdProveedor.grid(row=1,column=0,pady=(0,20),padx=(30,20))
    entryIdProveedor = Entry(frameDetallesProveedor,font=("Calibri",15),width=25,state="readonly")
    entryIdProveedor.grid(row=1,column=1,pady=(0,20),padx=(30,20))
    labelRazonSocialProveedor = Label(frameDetallesProveedor,text="Razón Social",font=("Calibri",15),width=15)
    labelRazonSocialProveedor.grid(row=2,column=0,pady=(0,20),padx=(30,20))
    entryRazonSocialProveedor = Entry(frameDetallesProveedor,font=("Calibri",15),width=25)
    entryRazonSocialProveedor.grid(row=2,column=1,pady=(0,20))  
    labelCuitProveedor = Label(frameDetallesProveedor,text="CUIT",font=("Calibri",15),width=15)
    labelCuitProveedor.grid(row=8,column=0,pady=(0,20),padx=(30,20))
    entryCuitProveedor = Entry(frameDetallesProveedor,font=("Calibri",15),width=25)
    entryCuitProveedor.grid(row=8,column=1,pady=(0,20))
    labelDireccionProveedor = Label(frameDetallesProveedor,text="Dirección",font=("Calibri",15),width=15)
    labelDireccionProveedor.grid(row=3,column=0,pady=(0,20),padx=(30,20))
    entryDireccionProveedor = Entry(frameDetallesProveedor,font=("Calibri",15),width=25)
    entryDireccionProveedor.grid(row=3,column=1,pady=(0,20))
    labelLocalidadProveedor = Label(frameDetallesProveedor,text="Localidad",font=("Calibri",15),width=15)
    labelLocalidadProveedor.grid(row=4,column=0,pady=(0,20),padx=(30,20))
    entryLocalidadProveedor = Entry(frameDetallesProveedor,font=("Calibri",15),width=25)
    entryLocalidadProveedor.grid(row=4,column=1,pady=(0,20))    
    labelProvinciaProveedor = Label(frameDetallesProveedor,text="Provincia",font=("Calibri",15),width=15)
    labelProvinciaProveedor.grid(row=9,column=0,pady=(0,20),padx=(30,20))
    entryProvinciaProveedor = Entry(frameDetallesProveedor,font=("Calibri",15),width=25)
    entryProvinciaProveedor.grid(row=9,column=1,pady=(0,20))
    labelCodigoPostalProveedor = Label(frameDetallesProveedor,text="Código Postal",font=("Calibri",15),width=15)
    labelCodigoPostalProveedor.grid(row=5,column=0,pady=(0,20),padx=(30,20))
    entryCodigoPostalProveedor = Entry(frameDetallesProveedor,font=("Calibri",15),width=25)
    entryCodigoPostalProveedor.grid(row=5,column=1,pady=(0,20))
    labelTelefonoProveedor = Label(frameDetallesProveedor,text="Teléfono",font=("Calibri",15),width=15)
    labelTelefonoProveedor.grid(row=6,column=0,pady=(0,20),padx=(30,20))
    entryTelefonoProveedor = Entry(frameDetallesProveedor,font=("Calibri",15),width=25)
    entryTelefonoProveedor.grid(row=6,column=1,pady=(0,20))
    labelIvaProveedor = Label(frameDetallesProveedor,text="IVA",font=("Calibri",15),width=15)
    labelIvaProveedor.grid(row=7,column=0,pady=(0,20),padx=(30,20))
    entryIvaProveedor = Entry(frameDetallesProveedor,font=("Calibri",15),width=25)
    entryIvaProveedor.grid(row=7,column=1,pady=(0,20))

    labelComboBuscar = Label(frameDetallesArticulo,text="Elija cliente",font=("Calibri",15),fg="white",bg="#56837D")        
    comboBuscar = ttk.Combobox(frameDetallesArticulo,width=15,font=("Calibri",15))
    entryBuscarArticulo = Entry(frameDetallesArticulo,font=("Calibri",15),width=40)
    entryBuscarArticulo.grid(row=0,column=0,columnspan=2,pady=(10,20),padx=(50,20))
    botonBuscarArticulo = Button(frameDetallesArticulo,text="Buscar",font=("Calibri",15),command=buscarProveedor,width=10,height=1)
    botonBuscarArticulo.grid(row=0,column=2,sticky=W,pady=(10,20))
    labelIdArticulo = Label(frameDetallesArticulo,text="ID",font=("Calibri",15),width=15)
    labelIdArticulo.grid(row=1,column=0,pady=(0,20),padx=(30,20))
    entryIdArticulo = Entry(frameDetallesArticulo,font=("Calibri",15),width=25,state="readonly")
    entryIdArticulo.grid(row=1,column=1,pady=(0,20),padx=(30,20))
    labelCodigoArticulo= Label(frameDetallesArticulo,text="Codigo",font=("Calibri",15),width=15)
    labelCodigoArticulo.grid(row=2,column=0,pady=(0,20),padx=(30,20))
    entryCodigoArticulo = Entry(frameDetallesArticulo,font=("Calibri",15),width=25)
    entryCodigoArticulo.grid(row=2,column=1,pady=(0,20))  
    labelCategoriaArticulo = Label(frameDetallesArticulo,text="Categoria",font=("Calibri",15),width=15)
    labelCategoriaArticulo.grid(row=3,column=0,pady=(0,20),padx=(30,20))
    entryCategoriaArticulo = Entry(frameDetallesArticulo,font=("Calibri",15),width=25)
    entryCategoriaArticulo.grid(row=3,column=1,pady=(0,20))
    
    labelStockArticulo = Label(frameDetallesArticulo,text="Stock",font=("Calibri",15),width=15)
    labelStockArticulo.grid(row=4,column=0,pady=(0,20),padx=(30,20))
    entryStockArticulo = Entry(frameDetallesArticulo,font=("Calibri",15),width=25)
    entryStockArticulo.grid(row=4,column=1,pady=(0,20))
    
    labelModeloArticulo = Label(frameDetallesArticulo,text="Modelo",font=("Calibri",15),width=15)
    labelModeloArticulo.grid(row=5,column=0,pady=(0,20),padx=(30,20))
    entryModeloArticulo = Entry(frameDetallesArticulo,font=("Calibri",15),width=25)
    entryModeloArticulo.grid(row=5,column=1,pady=(0,20))
    labelPrecioCostoArticulo = Label(frameDetallesArticulo,text="Precio C.",font=("Calibri",15),width=15)
    labelPrecioCostoArticulo.grid(row=6,column=0,pady=(0,20),padx=(30,20))
    entryPrecioCostoArticulo = Entry(frameDetallesArticulo,font=("Calibri",15),width=25)
    entryPrecioCostoArticulo.grid(row=6,column=1,pady=(0,20))
    labelPrecioVentaArticulo = Label(frameDetallesArticulo,text="Precio Venta",font=("Calibri",15),width=15)
    labelPrecioVentaArticulo.grid(row=7,column=0,pady=(0,20),padx=(30,20))
    entryPrecioVentaArticulo = Entry(frameDetallesArticulo,font=("Calibri",15),width=25)
    entryPrecioVentaArticulo.grid(row=7,column=1,pady=(0,20))
    labelMarcaArticulo = Label(frameDetallesArticulo,text="Marca",font=("Calibri",15),width=15)
    labelMarcaArticulo.grid(row=8,column=0,pady=(0,20),padx=(30,20))
    entryMarcaArticulo = Entry(frameDetallesArticulo,font=("Calibri",15),width=25)
    entryMarcaArticulo.grid(row=8,column=1,pady=(0,20))
    

    tablaListarClientes = ttk.Treeview(frameListarClientes)
    tablaListarClientes.place(x=10,y=10,width=781,height=500)
    estilos = ttk.Style()
    estilos.configure("Treeview.Heading",font=("Calibri bold",9),foreground="blue")

    tablaListarProveedor = ttk.Treeview(frameListarProveedor)
    tablaListarProveedor.place(x=10,y=10,width=781,height=500)
    estilos = ttk.Style()
    estilos.configure("Treeview.Heading",font=("Calibri bold",9),foreground="blue")

    tablaListarArticulo = ttk.Treeview(frameListarArticulo)
    tablaListarArticulo.place(x=10,y=10,width=781,height=500)
    estilos = ttk.Style()
    estilos.configure("Treeview.Heading",font=("Calibri bold",9),foreground="blue")

     
    tablaListarClientes["columns"] = ("razonSocialCliente","cuitCliente","direccionCliente","localidadCliente","provinciaCliente","codigoPostalCliente","telefonoCliente","ivaCliente")
    tablaListarClientes.column("#0",width=24)
    tablaListarClientes.heading("#0",text="ID")
    tablaListarClientes.column("razonSocialCliente",width=110)
    tablaListarClientes.heading("razonSocialCliente",text="Razon Social")
    tablaListarClientes.column("cuitCliente",width=80)
    tablaListarClientes.heading("cuitCliente",text="Cuit")
    tablaListarClientes.column("direccionCliente",width=100)
    tablaListarClientes.heading("direccionCliente",text="Direccion")
    tablaListarClientes.column("localidadCliente",width=55)
    tablaListarClientes.heading("localidadCliente",text="Localidad")
    tablaListarClientes.column("provinciaCliente",width=55)
    tablaListarClientes.heading("provinciaCliente",text="Provincia")
    tablaListarClientes.column("codigoPostalCliente",width=25)
    tablaListarClientes.heading("codigoPostalCliente",text="Cód. P.")
    tablaListarClientes.column("telefonoCliente",width=80)
    tablaListarClientes.heading("telefonoCliente",text="Teléfono")
    tablaListarClientes.column("ivaCliente",width=100)
    tablaListarClientes.heading("ivaCliente",text="IVA")

    tablaListarProveedor["columns"] = ("razonSocialProveedor","cuitProveedor","direccionProveedor","localidadProveedor","provinciaProveedor","codigoPostalProveedor","telefonoProveedor","ivaProveedor")
    tablaListarProveedor.column("#0",width=24)
    tablaListarProveedor.heading("#0",text="ID")
    tablaListarProveedor.column("razonSocialProveedor",width=110)
    tablaListarProveedor.heading("razonSocialProveedor",text="Razon Social")
    tablaListarProveedor.column("cuitProveedor",width=80)
    tablaListarProveedor.heading("cuitProveedor",text="Cuit")
    tablaListarProveedor.column("direccionProveedor",width=100)
    tablaListarProveedor.heading("direccionProveedor",text="Direccion")
    tablaListarProveedor.column("localidadProveedor",width=55)
    tablaListarProveedor.heading("localidadProveedor",text="Localidad")
    tablaListarProveedor.column("provinciaProveedor",width=55)
    tablaListarProveedor.heading("provinciaProveedor",text="Provincia")
    tablaListarProveedor.column("codigoPostalProveedor",width=25)
    tablaListarProveedor.heading("codigoPostalProveedor",text="Cód. P.")
    tablaListarProveedor.column("telefonoProveedor",width=80)
    tablaListarProveedor.heading("telefonoProveedor",text="Teléfono")
    tablaListarProveedor.column("ivaProveedor",width=100)
    tablaListarProveedor.heading("ivaProveedor",text="IVA")

    tablaListarArticulo["columns"] = ("codigoArticulo","marcaArticulo","modeloArticulo","categoriaArticulo","stockArticulo","precioCosto","precioVenta")
    tablaListarArticulo.column("#0",width=24)
    tablaListarArticulo.heading("#0",text="ID")
    tablaListarArticulo.column("codigoArticulo",width=110)
    tablaListarArticulo.heading("marcaArticulo",text="Razon Social")
    tablaListarArticulo.column("modeloArticulo",width=80)
    tablaListarArticulo.heading("categoriaArticulo",text="Cuit")
    tablaListarArticulo.column("stockArticulo",width=100)
    tablaListarArticulo.heading("precioCosto",text="Direccion")
    tablaListarArticulo.column("precioVenta",width=55)
    
    def guardarCliente():
        datos = (entryRazonSocialCliente.get(),entryCuitCliente.get(),entryDireccionCliente.get(),entryLocalidadCliente.get(),entryProvinciaCliente.get(),entryCodigoPostalCliente.get(),entryTelefonoCliente.get(),entryIvaCliente.get())
        if(vacios(datos)):
            if(soloLetras(datos[0]) and soloNumeros(datos[6])):              
                tabla = conexion.cursor()
                sql = "INSERT INTO clientes(razonSocialCliente,cuitCliente,direccionCliente,localidadCliente,provinciaCliente,codigoPostalCliente,telefonoCliente,ivaCliente) VALUES(?,?,?,?,?,?,?,?)"
                tabla.execute(sql,datos)
                conexion.commit()
                tabla.close()
                messagebox.showinfo("Sistema","Se a guardado")
                vaciarEntryCliente()
            else:
                messagebox.showinfo("Sistema","Algún dato esta incorrecto")
        else:
            messagebox.showinfo("Sistema","Complete los campos")
    def guardarProveedor():
        datosP = (entryRazonSocialProveedor.get(),entryCuitProveedor.get(),entryDireccionProveedor.get(),entryLocalidadProveedor.get(),entryProvinciaProveedor.get(),entryCodigoPostalProveedor.get(),entryTelefonoProveedor.get(),entryIvaProveedor.get())
        if(vacios(datosP)):
            if(soloLetras(datosP[0]) and soloNumeros(datosP[6])):              
                tablaP = conexion.cursor()
                sqlP = "INSERT INTO proveedores(razonSocialProveedor,cuitProveedor,direccionProveedor,localidadProveedor,provinciaProveedor,codigoPostalProveedor,telefonoProveedor,ivaProveedor) VALUES(?,?,?,?,?,?,?,?)"
                tablaP.execute(sqlP,datosP)
                conexion.commit()
                tablaP.close()
                messagebox.showinfo("Sistema","Se a guardado")
                vaciarEntryProveedor()
            else:
                messagebox.showinfo("Sistema","Algún dato esta incorrecto")
        else:
            messagebox.showinfo("Sistema","Complete los campos")
            ######################################################################################################################33
    def guardarArticulo():
        datosA = (entryCodigoArticulo.get(),entryMarcaArticulo.get(),entryModeloArticulo.get(),entryCategoriaArticulo.get(),entryStockArticulo.get(),entryPrecioCostoArticulo.get(),entryPrecioVentaArticulo.get())
        if(vacios(datosA)):
            if(soloLetras(datosA[1]) and soloNumeros(datosA[0])):              
                tablaA = conexion.cursor()
                sqlA = "INSERT INTO articulos(codigoArticulo,marcaArticulo,modeloArticulo,categoriaArticulo,stockArticulo,precioCosto,precioCosto) VALUES(?,?,?,?,?,?,?)"
                tablaA.execute(sqlA,datosA)
                conexion.commit()
                tablaA.close()
                messagebox.showinfo("Sistema","Se a guardado")
                vaciarEntryArticulo()
            else:
                messagebox.showinfo("Sistema","Algún dato esta incorrecto")
        else:
            messagebox.showinfo("Sistema","Complete los campos")
    def modificarArticulo():
        entryIdArticulo.config(state="normal")
        datosA = (entryCodigoArticulo.get(),entryMarcaArticulo.get(),entryModeloArticulo.get(),entryCategoriaArticulo.get(),entryStockArticulo.get(),entryPrecioCostoArticulo.get(),entryPrecioVentaArticulo.get())
        entryIdArticulo.config(state="readonly")
        if(datos[7] != ""):
            if(vacios(datosA)):
              tablaA = conexion.cursor()          
              sqlA = "UPDATE articulos SET codigoArticulo=?,marcaArticulo=?,modeloArticulo=?,categoriaArticulo=?,stockArticulo=?,precioCosto=?,telefonoCliente=? WHERE idArticulo=?"
              tablaA.execute(sqlA,datosA)
              conexion.commit()
              tablaA.close()
              messagebox.showinfo("Sistema","Se a modificado")
              vaciarEntryArticulo()
            else:
              messagebox.showinfo("Sistema","Error, complete los campos")            
        else:
            messagebox.showwarning("Sistema","ERROR! Busque dato a modificar")
    def modificarCliente():
        entryIdCliente.config(state="normal")
        datos = (entryRazonSocialCliente.get(),entryCuitCliente.get(),entryDireccionCliente.get(),entryLocalidadCliente.get(),entryProvinciaCliente.get(),entryCodigoPostalCliente.get(),entryTelefonoCliente.get(),entryIvaCliente.get(),entryIdCliente.get())
        entryIdCliente.config(state="readonly")
        if(datos[8] != ""):
            if(vacios(datos)):
              tabla = conexion.cursor()          
              sql = "UPDATE clientes SET razonSocialCliente=?,cuitCliente=?,direccionCliente=?,localidadCliente=?,provinciaCliente=?,codigoPostalCliente=?,telefonoCliente=?,ivaCliente=? WHERE idCliente=?"
              tabla.execute(sql,datos)
              conexion.commit()
              tabla.close()
              messagebox.showinfo("Sistema","Se a modificado")
              vaciarEntryCliente()
            else:
              messagebox.showinfo("Sistema","Error, complete los campos")            
        else:
            messagebox.showwarning("Sistema","ERROR! Busque dato a modificar")
  
    def modificarProveedor():
        entryIdProveedor.config(state="normal")
        datosP = (entryRazonSocialProveedor.get(),entryCuitProveedor.get(),entryDireccionProveedor.get(),entryLocalidadProveedor.get(),entryProvinciaProveedor.get(),entryCodigoPostalProveedor.get(),entryTelefonoProveedor.get(),entryIvaProveedor.get(),entryIdProveedor.get())
        entryIdProveedor.config(state="readonly")
##        if(datosP[8] != ""):
        if(vacios(datosP)):
              tablaP = conexion.cursor()          
              sqlP="UPDATE proveedores SET razonSocialProveedor=?,cuitProveedor=?,direccionProveedor=?,localidadProveedor=?,provinciaProveedor=?,codigoPostalProveedor=?,telefonoProveedor=?,ivaProveedor=? WHERE idProveedor=?"
              tablaP.execute(sqlP,datosP)
              conexion.commit()
              tablaP.close()
              messagebox.showinfo("Sistema","Se a modificado")
              vaciarEntryProveedor()
        else:
              messagebox.showinfo("Sistema","Error, complete los campos")            
##        else:
##            messagebox.showwarning("Sistema","ERROR! Busque dato a modificar")
    def listarFrameCliente():
        frameListarClientes.place(x=0,y=0,width=800,height=450)
        frameDetallesClientes.place_forget()
        botonGuardarCliente.grid_forget()
        botonModificarCliente.grid_forget()
        botonListarCliente.grid_forget()
        botonBorrarCliente.grid_forget()           
        botonDetallesCliente.grid(row=0,column=3,padx=20,pady=10)
##        botonInicioCliente.grid(row=0,column=4,padx=20,pady=15)
        tabla = conexion.cursor()
        sql="SELECT idCliente,razonSocialCliente,cuitCliente,cuitCliente,localidadCliente,provinciaCliente,codigoPostalCliente,telefonoCliente,ivaCliente FROM clientes"
        tabla.execute(sql)       
        datosListar = tabla.fetchall()
        for filas in tablaListarClientes.get_children(): ## elimimanos tablas
            tablaListarClientes.delete(filas)
        for dato in datosListar:
            tablaListarClientes.insert("",END,text=dato["idCliente"],values=(dato["razonSocialCliente"],dato["cuitCliente"],dato["cuitCliente"],dato["localidadCliente"],dato["provinciaCliente"],dato["codigoPostalCliente"],dato["telefonoCliente"],dato["ivaCliente"]))

    def listarFrameProveedor():
        frameListarProveedor.place(x=0,y=0,width=800,height=450)
        frameDetallesProveedor.place_forget()
        botonGuardarProveedor.grid_forget()
        botonModificarProveedor.grid_forget()
        botonListarProveedor.grid_forget()
        botonBorrarProveedor.grid_forget()           
        botonDetallesProveedor.grid(row=0,column=3,padx=20,pady=10)
##        botonInicioCliente.grid(row=0,column=4,padx=20,pady=15)
        tablaP = conexion.cursor()
        sqlP="SELECT idProveedor,razonSocialProveedor,cuitProveedor,cuitProveedor,localidadProveedor,provinciaProveedor,codigoPostalProveedor,telefonoProveedor,ivaProveedor FROM proveedores"
        tablaP.execute(sqlP)       
        datosListarP = tablaP.fetchall()
        for filasP in tablaListarProveedor.get_children(): ## elimimanos tablas
            tablaListarProveedor.delete(filasP)
        for datoP in datosListarP:
            tablaListarProveedor.insert("",END,text=datoP["idProveedor"],values=(datoP["razonSocialProveedor"],datoP["cuitProveedor"],datoP["cuitProveedor"],datoP["localidadProveedor"],datoP["provinciaProveedor"],datoP["codigoPostalProveedor"],datoP["telefonoProveedor"],datoP["ivaProveedor"]))

        
    def inicioCliente():
        cerrarFrames()
        frameBotones.place(x=0,y=0,width=200,height=600)
        vaciarEntryCliente()
    def inicioProveedor():
        cerrarFrames()
        frameBotones.place(x=0,y=0,width=200,height=600)
        vaciarEntryProveedor()

    def detallesCliente():
        botonDetallesCliente.grid_forget()
        frameDetallesClientes.place(x=0,y=0,width=900,height=500)#frameClientes
        botonGuardarCliente.grid(row=0,column=0,padx=20,pady=10)
        botonModificarCliente.grid(row=0,column=1,padx=20,pady=10)
        botonBorrarCliente.grid(row=0,column=2,padx=20,pady=10)
        botonListarCliente.grid(row=0,column=3,padx=20,pady=10)
##        botonInicioCliente.grid(row=0,column=4,padx=20,pady=10)       
        frameListarClientes.place_forget()
    def detallesProveedor():
        botonDetallesProveedor.grid_forget()
        frameDetallesProveedor.place(x=0,y=0,width=900,height=500)#frameClientes
        botonGuardarProveedor.grid(row=0,column=0,padx=20,pady=10)
        botonModificarProveedor.grid(row=0,column=1,padx=20,pady=10)
        botonBorrarProveedor.grid(row=0,column=2,padx=20,pady=10)
        botonListarProveedor.grid(row=0,column=3,padx=20,pady=10)
##        botonInicioCliente.grid(row=0,column=4,padx=20,pady=10)       
        frameListarProveedor.place_forget()
    botonGuardarCliente = Button(frameBotonesClientes,text="Guardar",font=("Calibri",16),command=guardarCliente,width=8,height=1,relief="flat",bg="powderblue")
    botonGuardarCliente.grid(row=0,column=0,padx=20,pady=10)
    botonModificarCliente = Button(frameBotonesClientes,text="Modificar",font=("Calibri",16),command=modificarCliente,width=8,height=1,relief="flat",bg="powderblue")
    botonModificarCliente.grid(row=0,column=1,padx=20,pady=10)    
    botonBorrarCliente = Button(frameBotonesClientes,text="Borrar",font=("Calibri",16),command=vaciarEntryCliente,width=8,height=1,relief="flat",bg="powderblue")
    botonBorrarCliente.grid(row=0,column=2,padx=20,pady=10)
    botonListarCliente = Button(frameBotonesClientes,text="Listar",font=("Calibri",16),command=listarFrameCliente,width=8,height=1,relief="flat",bg="powderblue")
    botonListarCliente.grid(row=0,column=3,padx=20,pady=10)
##    botonInicioCliente = Button(frameBotonesClientes,text="Inicio",font=("Calibri",16),command=inicioCliente,width=8,height=1,relief="flat",bg="powderblue")
##    botonInicioCliente.grid(row=0,column=4,padx=20,pady=10)    
    botonDetallesCliente = Button(frameBotonesClientes,text="Detalle",font=("Calibri",16),command=detallesCliente,width=8,height=1,relief="flat",bg="powderblue") 
                                 
    botonGuardarProveedor = Button(frameBotonesProveedor,text="Guardar",font=("Calibri",16),command=guardarProveedor,width=8,height=1,relief="flat",bg="powderblue")
    botonGuardarProveedor.grid(row=0,column=0,padx=20,pady=10)
    botonModificarProveedor = Button(frameBotonesProveedor,text="Modificar",font=("Calibri",16),command=modificarProveedor,width=8,height=1,relief="flat",bg="powderblue")
    botonModificarProveedor.grid(row=0,column=1,padx=20,pady=10)    
    botonBorrarProveedor = Button(frameBotonesProveedor,text="Borrar",font=("Calibri",16),command=vaciarEntryProveedor,width=8,height=1,relief="flat",bg="powderblue")
    botonBorrarProveedor.grid(row=0,column=2,padx=20,pady=10)
    botonListarProveedor = Button(frameBotonesProveedor,text="Listar",font=("Calibri",16),command=listarFrameProveedor,width=8,height=1,relief="flat",bg="powderblue")
    botonListarProveedor.grid(row=0,column=3,padx=20,pady=10)
##    botonInicioCliente = Button(frameBotonesClientes,text="Inicio",font=("Calibri",16),command=inicioCliente,width=8,height=1,relief="flat",bg="powderblue")
##    botonInicioCliente.grid(row=0,column=4,padx=20,pady=10)    
    botonDetallesProveedor = Button(frameBotonesProveedor,text="Detalle",font=("Calibri",16),command=detallesProveedor,width=8,height=1,relief="flat",bg="powderblue") 
                                 
    botonGuardarArticulo = Button(frameBotonesArticulo,text="Guardar",font=("Calibri",16),command=guardarArticulo,width=8,height=1,relief="flat",bg="powderblue")
    botonGuardarArticulo.grid(row=0,column=0,padx=20,pady=10)
    botonModificarArticulo = Button(frameBotonesArticulo,text="Modificar",font=("Calibri",16),command=modificarArticulo,width=8,height=1,relief="flat",bg="powderblue")
    botonModificarArticulo.grid(row=0,column=1,padx=20,pady=10)    
    botonBorrarArticulo = Button(frameBotonesProveedor,text="Borrar",font=("Calibri",16),command=vaciarEntryArticulo,width=8,height=1,relief="flat",bg="powderblue")
    botonBorrarArticulo.grid(row=0,column=2,padx=20,pady=10)
##    botonListarArticulo = Button(frameBotonesProveedor,text="Listar",font=("Calibri",16),command=listarFrameArticulo,width=8,height=1,relief="flat",bg="powderblue")
##    botonListarArticulo.grid(row=0,column=3,padx=20,pady=10)
##    botonInicioCliente = Button(frameBotonesClientes,text="Inicio",font=("Calibri",16),command=inicioCliente,width=8,height=1,relief="flat",bg="powderblue")
##    botonInicioCliente.grid(row=0,column=4,padx=20,pady=10)    
##    botonDetallesArticulo = Button(frameBotonesProveedor,text="Detalle",font=("Calibri",16),command=detallesArticulo,width=8,height=1,relief="flat",bg="powderblue") 
                                 




##PROVEEEDORES
    
    
    
    
    frameVentas = Frame(ventana,bg="green")
    
    frameCompras = Frame(ventana,bg="pink")

    



    
#FUNCION BOTONES
    def cerrarFrames():
        frameProveedor.place_forget()
        frameArticulo.place_forget()
        frameCompras.place_forget()
        frameVentas.place_forget()
        frameClientes.place_forget()
        
    def mostrarClientes(evento):
        cerrarFrames()
        
        frameClientes.place(x=200,y=0,width=1000,height=600)
        
    def mostrarProveedor():
        cerrarFrames()
        frameProveedor.place(x=200,y=0,width=1000,height=600)

    def mostrarArticulo(evento):
        cerrarFrames()
        frameArticulo.place(x=200,y=0,width=1000,height=600)
        
    def mostrarVentas(evento):
        cerrarFrames()
        frameVentas.place(x=200,y=0,width=1000,height=600)
        
    def mostrarCompras(evento):
        cerrarFrames()
        frameCompras.place(x=200,y=0,width=1000,height=600)

    def mostrarHome(evento):
        cerrarFrames()
#BOTONES
    botonCliente = Button(frameBotones,text="Clientes",font=("Calibri",15),width=15,height=2)
    botonCliente.grid(row=0,column=0,padx=20,pady=20)
    botonCliente.bind("<Button-1>",mostrarClientes)    
    botonProveedor = Button(frameBotones,text="Proveedores",font=("Calibri",15),width=15,height=2,command=mostrarProveedor)
    botonProveedor.grid(row=1,column=0,padx=20,pady=20)
    botonArticulo = Button(frameBotones,text="Articulos",font=("Calibri",15),width=15,height=2)
    botonArticulo.grid(row=2,column=0,padx=20,pady=20)
    botonArticulo.bind("<Button-1>",mostrarArticulo)
    botonVentas = Button(frameBotones,text="Ventas",font=("Calibri",15),width=15,height=2)
    botonVentas.grid(row=3,column=0,padx=20,pady=20)
    botonVentas.bind("<Button-1>",mostrarVentas)    
    botonCompras = Button(frameBotones,text="Compras",font=("Calibri",15),width=15,height=2)
    botonCompras.grid(row=4,column=0,padx=20,pady=(0,20))
    botonCompras.bind("<Button-1>",mostrarCompras)
    botonHome = Button(frameBotones,text="Home",font=("Calibri",15),width=15,height=1)
    botonHome.grid(row=5,column=0,padx=20,pady=(0,20))
    botonHome.bind("<Button-1>",mostrarHome)

    
    ventana.mainloop()

ventanaPrincipal()

























