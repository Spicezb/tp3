# Realizado Por Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado
# Fecha de inicio 15/05/2025 a las 18:00
# Última modificación 26/06/2025 02:30
# Versión de Python 3.13.2

# Importaciones de Librerías
from tkinter import *
from funciones import *
from tkinter import ttk
import main

def ventanaEstxEstado(lista):
    """
    Funcionamiento:
    - Crea una ventana para mostrar una estadística de los animales agrupados por estado.
    - Obtiene la cantidad y porcentaje de animales en cada estado mediante la función estaXEstado.
    - Para cada estado, crea y muestra dos etiquetas que muestran la cantidad y el porcentaje correspondiente.
    Entradas:
    - lista (list): Lista de objetos `Animal` cuyo estado será analizado para generar las estadísticas.
    Salidas:
    - Muestra la ventana con las estadísticas de cantidad y porcentaje por estado de los animales.
    """
    y=280
    y2=280
    cantidades=estaXEstado(lista)
    vtnEstxEstado= Toplevel()
    vtnEstxEstado.configure(bg="#3C5520")
    vtnEstxEstado.title("Estadistica por estado")
    vtnEstxEstado.geometry("1090x850+0+0")
    vtnEstxEstado.iconbitmap("imagenes/icono.ico")
    vtnEstxEstado.resizable(0,0)
    imgFondo=PhotoImage(file="imagenes/fondoEstxEstado.png")
    lblFondo=Label(vtnEstxEstado,image=imgFondo)
    lblFondo.image_names=imgFondo
    lblFondo.place(x=-2,y=-2)
    for i,(cantidad,porcentaje) in enumerate(cantidades):
        lbl1=Label(vtnEstxEstado, text=(cantidad),width=4, font=("Fixedsys", 26),fg="#f7c760",bg="#6d4224")
        lbl2=Label(vtnEstxEstado, text=f"{porcentaje}%",width=5,font=("Fixedsys", 26),fg="#f7c760",bg="#6d4224")
        lbl1.grid(row=i, column=0)
        lbl2.grid(row=i, column=1)
        lbl1.place(x=600,y=y)
        lbl2.place(x=750,y=y2)
        y+=80
        y2+=80

def ventanaHTML(lista):
    """
    Funcionamiento:
    - Crea una ventana emergente que pregunta al usuario si desea generar un archivo HTML con las estadísticas de los animales.
    Entradas:
    - lista (list): Lista de animales cuyos datos se exportarán al archivo HTML.
    Salidas:
    - La función generarCSV crea el archivo HTML con la información de los animales.
    """
    vtnHTML = Toplevel()
    vtnHTML.title("Generar HTML")
    vtnHTML.geometry("794x445")
    vtnHTML.configure(bg="#3C5520")
    vtnHTML.iconbitmap("imagenes/icono.ico")
    vtnHTML.resizable(0,0)
    imgHTML=PhotoImage(file="imagenes/fondoHTML.png")
    imgBtnCancelar=PhotoImage(file="imagenes/btnCancelar.png")
    imgBtnAceptar=PhotoImage(file="imagenes/btnAceptar.png")
    lblFondo=Label(vtnHTML,image=imgHTML)
    lblTitulo=Label(vtnHTML,text="¿Desea generar un HTML con las\n estadisticas de los animales?",bg="#193214",fg="#f7c760",font=("Fixedsys", 18))
    btnCancelar=Button(vtnHTML,image=imgBtnCancelar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: vtnHTML.destroy())
    btnAceptar=Button(vtnHTML,image=imgBtnAceptar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: html(lista,vtnHTML))
    lblFondo.image_names=imgHTML
    btnCancelar.image_names=imgBtnCancelar
    btnAceptar.image_names=imgBtnAceptar
    lblFondo.place(x=-2,y=-2)
    lblTitulo.place(x=150,y=120)
    btnCancelar.place(x=450,y=250)
    btnAceptar.place(x=150,y=250)

def ventanaPDF(lista):
    """
    Funcionamiento:
    - Crea una ventana emergente que pregunta al usuario si desea generar un archivo PDF con las calificaciones de los animales.
    Entradas:
    - lista (list): Lista de animales cuyos datos se exportarán al archivo PDF.
    Salidas:
    - La función generarCSV crea el archivo PDF con la información de los animales.
    """
    vtnPDF = Toplevel()
    vtnPDF.title("Generar PDF")
    vtnPDF.geometry("794x445")
    vtnPDF.configure(bg="#3C5520")
    vtnPDF.iconbitmap("imagenes/icono.ico")
    vtnPDF.resizable(0,0)
    imgHTML=PhotoImage(file="imagenes/fondoPDF.png")
    imgBtnCancelar=PhotoImage(file="imagenes/btnCancelar.png")
    imgBtnAceptar=PhotoImage(file="imagenes/btnAceptar.png")
    lblFondo=Label(vtnPDF,image=imgHTML)
    lblTitulo=Label(vtnPDF,text="¿Desea generar un PDF con las\n estadisticas de los animales?",bg="#193214",fg="#f7c760",font=("Fixedsys", 18))
    btnCancelar=Button(vtnPDF,image=imgBtnCancelar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: vtnPDF.destroy())
    btnAceptar=Button(vtnPDF,image=imgBtnAceptar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: pdf(lista,vtnPDF))
    lblFondo.image_names=imgHTML
    btnCancelar.image_names=imgBtnCancelar
    btnAceptar.image_names=imgBtnAceptar
    lblFondo.place(x=-2,y=-2)
    lblTitulo.place(x=150,y=120)
    btnCancelar.place(x=450,y=250)
    btnAceptar.place(x=150,y=250)

def ventanaCSV(lista):
    """
    Funcionamiento:
    - Crea una ventana emergente que pregunta al usuario si desea generar un archivo CSV con las estadísticas de los animales.
    Entradas:
    - lista (list): Lista de animales cuyos datos se exportarán al archivo CSV.
    Salidas:
    - La función generarCSV crea el archivo CSV con la información de los animales.
    """
    vtnCSV = Toplevel()
    vtnCSV.title("Generar CSV")
    vtnCSV.geometry("794x445")
    vtnCSV.configure(bg="#3C5520")
    vtnCSV.iconbitmap("imagenes/icono.ico")
    vtnCSV.resizable(0,0)
    imgHTML=PhotoImage(file="imagenes/fondoCSV.png")
    imgBtnCancelar=PhotoImage(file="imagenes/btnCancelar.png")
    imgBtnAceptar=PhotoImage(file="imagenes/btnAceptar.png")
    lblFondo=Label(vtnCSV,image=imgHTML)
    lblTitulo=Label(vtnCSV,text="¿Desea generar un CVS con las\n estadisticas de los animales?",bg="#193214",fg="#f7c760",font=("Fixedsys", 18))
    btnCancelar=Button(vtnCSV,image=imgBtnCancelar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: vtnCSV.destroy())
    btnAceptar=Button(vtnCSV,image=imgBtnAceptar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: generarCSV(lista,vtnCSV))
    lblFondo.image_names=imgHTML
    btnCancelar.image_names=imgBtnCancelar
    btnAceptar.image_names=imgBtnAceptar
    lblFondo.place(x=-2,y=-2)
    lblTitulo.place(x=150,y=120)
    btnCancelar.place(x=450,y=250)
    btnAceptar.place(x=150,y=250)

def ventanaMstInv(lista2):
    """
    Funcionamiento:
    - Crea una ventana secundaria para mostrar el inventario de animales.
    - Extrae las URLs de las imágenes de cada animal en la lista recibida y las almacena en una nueva lista..
    - Llama a la función mostrarInventario para desplegar el inventario con las imágenes y datos correspondientes.
    Entradas:
    - lista2 (list): Lista de objetos `Animal` desde la cual se extraen las URLs y datos para mostrar.
    Salidas:
    - Muestra la ventana con el inventario desplegado.
    """
    lista=[]
    for x in lista2:
        lol=x.getURL()
        lista.append(lol)
    main.cont+=1
    main.cont2+=1
    vtnMstInv= Toplevel()
    imgHTML=PhotoImage(file="imagenes/fondoMstInven.png")
    lblFondo=Label(vtnMstInv,image=imgHTML)
    lblFondo.image_names=imgHTML
    lblFondo.place(x=-2,y=-2)
    vtnMstInv.configure(bg="#3C5520")
    vtnMstInv.title("Inventario")
    vtnMstInv.geometry("1100x950+0+0")
    vtnMstInv.iconbitmap("imagenes/icono.ico")
    vtnMstInv.resizable(0,0)
    mostrarInventario(vtnMstInv,lista,lista2,main.cont-1,0)

def ventanaOrden(lista):
    """
    Funcionamiento:
    - Crea una ventana emergente para que el usuario seleccione un orden específico (Carnívoros, Herbívoros u Omnívoros) para generar un HTML con estadísticas de animales.
    Entradas:
    - lista (list): Lista de animales que será filtrada para generar el HTML.
    Salidas:
    - La función htmlOrdenAUX gestiona la generación del archivo HTML basado en la opción seleccionada.
    """
    vtnOrden = Toplevel()
    vtnOrden.title("Generar HTML eb orden")
    vtnOrden.geometry("794x445")
    vtnOrden.configure(bg="#3C5520")
    vtnOrden.iconbitmap("imagenes/icono.ico")
    vtnOrden.resizable(0,0)
    imgHTML=PhotoImage(file="imagenes/fondoHTML.png")
    imgBtnCancelar=PhotoImage(file="imagenes/btnCancelar.png")
    imgBtnAceptar=PhotoImage(file="imagenes/btnAceptar.png")
    lblFondo=Label(vtnOrden,image=imgHTML)
    lblTitulo=Label(vtnOrden,text="¿Desea generar un HTML con las\n estadisticas de los animales?",bg="#193214",fg="#f7c760",font=("Fixedsys", 18))
    lblORden=Label(vtnOrden,text="Orden:",bg="#193214",fg="#f7c760",font=("Fixedsys", 17))
    btnCancelar=Button(vtnOrden,image=imgBtnCancelar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: vtnOrden.destroy())
    cbxDeci=ttk.Combobox(vtnOrden, font=("Fixedsys", 24), width=10)
    lstDeci=["Carnívoros","Herbívoros","Omnívoros"]
    cbxDeci["values"]=lstDeci
    cbxDeci.delete(0, END)
    cbxDeci.configure(state="readonly")
    btnAceptar=Button(vtnOrden,image=imgBtnAceptar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: htmlOrdenAUX(cbxDeci.get(),lista,vtnOrden))
    lblFondo.image_names=imgHTML
    btnCancelar.image_names=imgBtnCancelar
    btnAceptar.image_names=imgBtnAceptar
    lblFondo.place(x=-2,y=-2)
    cbxDeci.place(x=380,y=194)
    lblORden.place(x=270,y=194)
    lblTitulo.place(x=150,y=120)
    btnCancelar.place(x=450,y=250)
    btnAceptar.place(x=150,y=250)

def ventanaCrearInven(lista,btnBtnMostrarInven,btnEstaXEstad,btnHtml,btnPDF,btnCSV,btnOrden,btn,btnCrearInven):
    """
    Funcionamiento:
    - Crea una ventana emergente para confirmar si el usuario desea generar un inventario con 20 animales.
    Entradas:
    - lista (list): Lista de animales que será utilizada para crear el inventario.
    Salidas:
    - La función crearInventario modifica la lista con el inventario generado.
    """
    vtnCrearInven = Toplevel()
    vtnCrearInven.title("Crear Inventario")
    vtnCrearInven.geometry("794x445")
    vtnCrearInven.configure(bg="#3C5520")
    vtnCrearInven.iconbitmap("imagenes/icono.ico")
    vtnCrearInven.resizable(0,0)
    imgHTML=PhotoImage(file="imagenes/fondoCI.png")
    imgBtnCancelar=PhotoImage(file="imagenes/btnCancelar.png")
    imgBtnAceptar=PhotoImage(file="imagenes/btnAceptar.png")
    lblFondo=Label(vtnCrearInven,image=imgHTML)
    lblTitulo=Label(vtnCrearInven,text="¿Desea generar un inventario\ncon 20 animales?",bg="#193214",fg="#f7c760",font=("Fixedsys", 18))
    btnCancelar=Button(vtnCrearInven,image=imgBtnCancelar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: vtnCrearInven.destroy())
    btnAceptar=Button(vtnCrearInven,image=imgBtnAceptar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: crearInventario(lista,vtnCrearInven,btnBtnMostrarInven,btnEstaXEstad,btnHtml,btnPDF,btnCSV,btnOrden,btn,btnCrearInven))
    lblFondo.image_names=imgHTML
    btnCancelar.image_names=imgBtnCancelar
    btnAceptar.image_names=imgBtnAceptar
    lblFondo.place(x=-2,y=-2)
    lblTitulo.place(x=150,y=120)
    btnCancelar.place(x=450,y=250)
    btnAceptar.place(x=150,y=250)

def vtnBuscar(lista,estado2):
    """
    Funcionamiento:
    - Crea una ventana secundaria para que el usuario ingrese la cantidad deseada de animales.
    Entradas:
    - lista (list): Lista que se devuelve sin modificar.
    - estado2 (tkinter.Widget): boton externo que se habilita.
    Salidas:
    - tuple: Retorna la tupla (lista, estado2) sin modificaciones.
    """
    vtnBsc = Toplevel()
    vtnBsc.geometry("1090x850+0+0")
    vtnBsc.resizable(0,0)
    vtnBsc.configure(bg="#193214")
    vtnBsc.title("Búsqueda de Animales")
    vtnBsc.iconbitmap("imagenes/icono.ico")
    imgFondo=PhotoImage(file="imagenes/fondoOL.png")
    
    imgBtnAceptar=PhotoImage(file="imagenes/btnAceptar.png")
    imgBtnCancelar=PhotoImage(file="imagenes/btnCancelar.png")

    lblFondo=Label(vtnBsc,image=imgFondo)
    lblCantidad=Label(vtnBsc, text="Cantidad\nDeseada:", fg="#f7c760", bg="#193214",font=("Fixedsys", 18))
    tbxCantidad = Entry(vtnBsc, font=("Fixedsys", 30), width=10, bd=3, relief="solid")
    btnAceptar=Button(vtnBsc,image=imgBtnAceptar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: obtenerLista(tbxCantidad.get(),vtnBsc,estado2))
    btnCancelar=Button(vtnBsc,image=imgBtnCancelar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: vtnBsc.destroy())
    
    btnAceptar.image_names=imgBtnAceptar
    btnCancelar.image_names=imgBtnCancelar
    lblFondo.image_names=imgFondo

    lblFondo.place(x=-2,y=-2)
    lblCantidad.place(x=350, y=350)
    tbxCantidad.place(x=500,y=350)
    btnAceptar.place(x=300,y=480)
    btnCancelar.place(x=600,y=480)
    return lista, estado2