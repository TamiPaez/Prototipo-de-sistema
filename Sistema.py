from Libraries.validaciones import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import random
#pillow(imagenes)
#reportlab(pdfs)
#cerberus(validaciones)
NOMBRE_PROGRAMA = "Ventas"
carrito = []
conexion = sqlite3.connect("bd/database.db")

def misEstilos():
	global estilos
	color_navegacion='#313642'
	color_navegacion2= '#434a5b'
	color_fondo = "#efefef"
	estilos = ttk.Style()
	estilos.theme_use("alt")
	estilos.configure("programa.TLabel",
					  background=color_navegacion,
					  foreground='snow',
					  font=('Calibri',24)
					 )
	estilos.configure("titulo.TLabel",
					  background= 'snow',
					  foreground='black',
					  font=('Calibri',24)
					 )
	estilos.configure("entradas.TLabel",
					  background='gray22',
					  foreground='snow',
					  font=('Calibri',13)
					 )
	estilos.configure("entradasCrud.TLabel",
					  background='snow',
					  foreground='black',
					  font=('Calibri',15)
					 )
	estilos.configure('login.TFrame',background='darkslateblue',relief=FLAT,border=0)
	estilos.configure('fondo.TFrame',background=color_fondo,relief=FLAT,border=0)
	estilos.configure('principal.TFrame',background='gray22',relief=FLAT,border=0)
	estilos.configure('navegacion.TFrame',background=color_navegacion,relief=FLAT,border=0)
	estilos.configure('transparente.TFrame',background=color_fondo,relief=FLAT,border=0)
	estilos.configure('blanco.TFrame',background="white",relief=FLAT,border=0)

	estilos.configure('botonNavegacion.TButton',
   					  background=color_navegacion,
   					  foreground='snow',
   					  font=('Calibri',13),
   					  relief=FLAT,
   					  bd=0,
					 )
	estilos.map('botonNavegacion.TButton',
		       background=[('pressed',color_navegacion2),('active',color_navegacion2)])
	estilos.configure('botonLogin.TButton',
					  background=color_navegacion,
   					  foreground='snow',
   					  font=('Calibri',13),
   					  relief=FLAT,
   					  bd=0,
					 )
	estilos.map('botonLogin.TButton',
		       background=[('pressed',color_navegacion2),('active',color_navegacion2)])
	estilos.configure('carrito.Treeview', rowheight=100)

	return estilos

def login():
	ventana.geometry("400x600")
	frame_login = ttk.Frame(ventana,style='login.TFrame')
	frame_login.pack(fill=BOTH,expand=1)
	def verificarLogin():
		frame_login.pack_forget()
		principal()
	boton_login = ttk.Button(frame_login,text="Ingresar",style='botonLogin.TButton',command=verificarLogin)
	boton_login.pack(side=BOTTOM,pady=40)

def principal():
	ventana.state("zoomed")
	frame_botones= ttk.Frame(ventana,style='navegacion.TFrame')
	frame_botones.pack(side=LEFT,fill=Y)
	frame_contenido = ttk.Frame(ventana,style='principal.TFrame')
	frame_contenido.pack(side=LEFT,fill=BOTH,expand=1)

	titulo_programa = ttk.Label(frame_botones,text=NOMBRE_PROGRAMA,anchor="c",justify=RIGHT,style="programa.TLabel")
	titulo_programa.pack(fill=X)
	inicio(frame_contenido)
	def verInicio():
		borrarFrames()
		if 'frame_inicio' not in globals():
			inicio(frame_contenido)
		else:
			frame_inicio.pack(fill=BOTH,expand=1)
	boton_inicio = ttk.Button(frame_botones,text='Inicio',style='botonNavegacion.TButton',command=verInicio)
	boton_inicio.pack(ipady=20,ipadx=10)
	def verArticulos():
		borrarFrames()
		if 'frame_articulos' not in globals():
			articulos(frame_contenido)
		else:
			frame_articulos.pack(fill=BOTH,expand=1)
	boton_Articulos = ttk.Button(frame_botones,text='Articulos',style='botonNavegacion.TButton',command=verArticulos)
	boton_Articulos.pack(ipady=20,ipadx=10)
	def verClientes():
		borrarFrames()
		if 'frame_clientes' not in globals():
			clientes(frame_contenido)
		else:
			frame_clientes.pack(fill=BOTH,expand=1)
	boton_clientes = ttk.Button(frame_botones,text='Clientes',style='botonNavegacion.TButton',command=verClientes)
	boton_clientes.pack(ipady=20,ipadx=10)
	def verProveedores():
		borrarFrames()
		if 'frame_proveedores' not in globals():
			proveedores(frame_contenido)
		else:
			frame_proveedores.pack(fill=BOTH,expand=1)
	boton_proveedores = ttk.Button(frame_botones,text='Proveedores',style='botonNavegacion.TButton',command=verProveedores)
	boton_proveedores.pack(ipady=20,ipadx=10)
	def verCompras():
		borrarFrames()
		if 'frame_compras' not in globals():
			compras(frame_contenido)
		else:
			frame_compras.pack(fill=BOTH,expand=1)
	boton_compras = ttk.Button(frame_botones,text='Compras',style='botonNavegacion.TButton',command=verCompras)
	boton_compras.pack(ipady=20,ipadx=10)
	def verVentas():
		borrarFrames()
		if 'frame_ventas' not in globals():
			ventas(frame_contenido)
		else:
			frame_ventas.pack(fill=BOTH,expand=1)
	boton_ventas = ttk.Button(frame_botones,text='Ventas',style='botonNavegacion.TButton',command=verVentas)
	boton_ventas.pack(ipady=20,ipadx=10)

def borrarFrames():
	if 'frame_inicio' in globals():
		frame_inicio.pack_forget()
	if 'frame_articulos' in globals():
		frame_articulos.pack_forget()
	if 'frame_clientes' in globals():
		frame_clientes.pack_forget()
	if 'frame_proveedores' in globals():
		frame_proveedores.pack_forget()
	if 'frame_compras' in globals():
		frame_compras.pack_forget()
	if 'frame_ventas' in globals():
		frame_ventas.pack_forget()
	
def inicio(frame_contenido):
	global frame_inicio
	frame_inicio = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_inicio.pack(fill=BOTH,expand=1)
	label_titulo = ttk.Label(frame_inicio,text="SISTEMA DE VENTAS",style='titulo.TLabel')
	label_titulo.pack()
	label_profe = ttk.Label(frame_inicio,text="Creado por el profe",style='entradas.TLabel')
	label_profe.pack(side=BOTTOM)

def articulos(frame_contenido):
	global frame_articulos
	frame_articulos = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_articulos.pack(fill=BOTH,expand=1)
	
	frame_buscador_articulos= ttk.Frame(frame_articulos,style='fondo.TFrame')
	frame_buscador_articulos.pack(side=LEFT,fill=BOTH,expand=1)
	frame_crud_articulos = ttk.Frame(frame_articulos,style='fondo.TFrame')
	frame_crud_articulos.pack(side=LEFT,fill=BOTH,expand=1)

	label_codigo = ttk.Label(frame_crud_articulos,text="Codigo",style="entradasCrud.TLabel")
	label_codigo.pack(anchor=W,padx=5)
	entry_codigo = ttk.Entry(frame_crud_articulos,font=("Calibri",15))
	entry_codigo.pack(anchor=W,padx=5)
	label_detalle = ttk.Label(frame_crud_articulos,text="Detalle",style="entradasCrud.TLabel")
	label_detalle.pack(anchor=W,padx=5)
	entry_detalle = ttk.Entry(frame_crud_articulos,font=("Calibri",15))
	entry_detalle.pack(anchor=W,padx=5)

	entry_buscador = ttk.Entry(frame_buscador_articulos,font=("Calibri",15))
	entry_buscador.pack(pady=10)
	tabla_articulos = ttk.Treeview(frame_buscador_articulos)
	tabla_articulos.pack(fill=BOTH,expand=1,padx=10,pady=10)
	tabla_articulos["columns"] = ("categoria","detalle")
	tabla_articulos.heading("#0",text="Codigo")
	tabla_articulos.heading("categoria",text="Categoria")
	tabla_articulos.heading("detalle",text="Detalle")

	def cargar_articulos():
		tabla = conexion.cursor()
		tabla.execute("SELECT * FROM articulos")
		datos = tabla.fetchall()
		tabla.close()
		for dato in datos:
			tabla_articulos.insert("",END,text=dato[0],values=(dato[2],))
	cargar_articulos()

	def buscar_articulo(evento):
		buscar = ('%' + entry_buscador.get() + '%',)
		tabla = conexion.cursor()
		tabla.execute("SELECT * FROM articulos WHERE detalle LIKE ? OR categoria LIKE (SELECT id FROM categorias WHERE nombre LIKE ?)", buscar)
		datos_articulos = tabla.fetchall()
		tabla.close()
		for fila in tabla_articulos.get_children():
			tabla_articulos.delete(fila)
		for dato in datos:
			tabla_articulos.insert("", END, text=dato[0], values=(dato[1], dato[2],))
	entry_buscador.bind("<KeyRelease>",buscar_articulo)
	
	def seleccionarArticulo(evento):
		index = tabla_articulos.selection()
		fila = tabla_articulos.item(index)
		codigo = fila["text"]
		tabla.execute("SELECT * FROM articulos WHERE codigo=?",codigo)
		datos_articulos=tabla.fetchall()
		id_categoria=(datos_articulos[0][1],)
		tabla.execute("SELECT * FROM categorias WHERE id=?",id_categoria)
		datos_categorias=tabla.fetchall()
		nombre_categoria=(datos_categorias[0][1],)
		tabla.close()
		borrar_entry_articulo()
		entry_detalle.delete(0,END)
		entry_detalle.insert(END,detalle)
		entry_codigo.delete(0,END)
		entry_codigo.insert(END,codigo)
	tabla_articulos.bind("<<TreeviewSelect>>",seleccionarArticulo)

def clientes(frame_contenido):
	global frame_clientes
	frame_clientes = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_clientes.pack(fill=BOTH,expand=1)
	label_clientes = ttk.Label(frame_clientes,text="Clientes",style='titulo.TLabel')
	label_clientes.pack()

def proveedores(frame_contenido):
	global frame_proveedores
	frame_proveedores = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_proveedores.pack(fill=BOTH,expand=1)
	label_proveedores = ttk.Label(frame_proveedores,text="Proveedores",style='titulo.TLabel')
	label_proveedores.pack()

def compras(frame_contenido):
	global frame_compras
	frame_compras = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_compras.pack(fill=BOTH,expand=1)
	label_compras = ttk.Label(frame_compras,text="Compras",style='titulo.TLabel')
	label_compras.pack()

def ventas(frame_contenido):
	global frame_ventas
	frame_ventas = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_ventas.pack(fill=BOTH,expand=1)

	frame_header = ttk.Frame(frame_ventas,style='transparente.TFrame')
	frame_header.pack(fill=X,ipady=50)
	frame_body = ttk.Frame(frame_ventas,style='transparente.TFrame')
	frame_body.pack(fill=BOTH,expand=1)

	frame_articulos = ttk.Frame(frame_body,style='blanco.TFrame')
	frame_articulos.pack(side=LEFT,fill=BOTH,expand=1,padx=(40,0),pady=10)
	frame_carrito = ttk.Frame(frame_body,style='blanco.TFrame')
	frame_carrito.pack(side=LEFT,fill=Y,ipadx=200,padx=40,pady=10)

	def ver(i,img):
		messagebox.showinfo("Ventas","Articulo "+str(i))
		articulo = ["Articulo "+str(i)]
		carrito.append(articulo)
		global img3
		img3 = img
		tabla_carrito.insert("",END,text="1",values=(i,"$500"),image=img)
	botones_articulos = []
	fila = 0
	columna = 0
	global img,img2
	img = PhotoImage(file='Assets/imagenes/burgerTest.png')
	img2= PhotoImage(file='Assets/imagenes/burgerTest1.png')
	imagenes = []
	imagenes.append(img)
	imagenes.append(img2)
	imagenes.append(img2)
	imagenes.append(img)
	imagenes.append(img)
	for i in range(1,6):
		codigo_art = random.randint(1,100000)
		boton = Button(frame_articulos,compound=TOP,image=imagenes[i-1],text="Articulo "+str(codigo_art),relief=FLAT,bg="gray",command=lambda nart=codigo_art,img=imagenes[i-1]:ver(nart,img))
		boton.grid(row=fila,column=columna,padx=5,pady=5)
		botones_articulos.append(boton)
		columna += 1 
		cant_columnas = 5
		if i % cant_columnas == 0:
			fila = fila + 1
			columna = 0

	#for boton in botones_articulos:
	#	boton["image"]="Assets/imagenes/burgerTest.png"
	"""
	fila = 0
	columna = 0
	for cantidadArticulos in range(1,10):
		botones_articulos[cantidadArticulos-1].grid(row=fila,column=columna,padx=5,pady=5)
		columna += 1 
		if cantidadArticulos % 5 == 0:
			fila = fila + 1
			columna = 0
	"""	
	tabla_carrito = ttk.Treeview(frame_carrito,style='carrito.Treeview')
	tabla_carrito.pack(side=TOP,fill=BOTH,expand=1)
	tabla_carrito["columns"] = ("detalle","precio")
	tabla_carrito.column("#0",width=100)
	tabla_carrito.column("detalle",width=200,stretch=False)
	tabla_carrito.column("precio",width=100,stretch=False)
	tabla_carrito.heading("#0",text="cantidad")
	tabla_carrito.heading("detalle",text="detalle")
	tabla_carrito.heading("precio",text="precio")
	def vender():
		for articulo in carrito:
			print(articulo)
	boton_vender = Button(frame_carrito,text="Vender",command=vender)
	boton_vender.pack(side=BOTTOM,pady=10,padx=10)
		
ventana = Tk()
misEstilos()
login()
ventana.mainloop()

