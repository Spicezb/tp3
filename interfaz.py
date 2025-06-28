# Realizado Por Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado
# Fecha de inicio 15/05/2025 a las 18:00
# Última modificación 26/06/2025 02:30
# Versión de Python 3.13.2

# Importaciones de Librerías
from tkinter import *
from funciones import *
from ventanasHijas import *
import main

cont=0
vtnPrincipal=Tk()

# Definicion de Funciones
def configVtnPrincipal(lista,estado1,estado2,estado3):
    if main.cont2==0:
        main.cont=0
    """
    Funcionamiento:
    - Es la ventana principal del programa.
    - Contiene los botones principales para cada función.
    Entradas:
    - N/A
    Salidas:
    - Muestra el menú principal del programa.
    """
    vtnPrincipal.configure(bg="#3C5520")
    vtnPrincipal.title("Zoo Inventario")
    vtnPrincipal.geometry("1090x850+0+0")
    vtnPrincipal.iconbitmap("imagenes/icono.ico")
    vtnPrincipal.resizable(0,0)
    imgFondo=PhotoImage(file="imagenes/fondoPrincipal.png")
    imgBtn=PhotoImage(file="imagenes/btnObtenerLista.png")
    imgBtnCrearInven=PhotoImage(file="imagenes/btnCrearInventario.png")
    imgBtnMostrarInven=PhotoImage(file="imagenes/btnMostrarInventario.png")
    imgBtnEstaXEstad=PhotoImage(file="imagenes/btnEstaXEstad.png")
    imgBtnHTML=PhotoImage(file="imagenes/btnHTML.png")
    imgBtnPDF=PhotoImage(file="imagenes/btnPDF.png")
    imgBtnCSV=PhotoImage(file="imagenes/btnCSV.png")
    imgBtnOrden=PhotoImage(file="imagenes/btnOrden.png")

    lblFondo=Label(vtnPrincipal,image=imgFondo)
    btn=Button(vtnPrincipal,image=imgBtn,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: vtnBuscar(lista,btnCrearInven),state=estado1)
    btnCrearInven=Button(vtnPrincipal,image=imgBtnCrearInven,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214",command=lambda: ventanaCrearInven(lista,btnBtnMostrarInven,btnEstaXEstad,btnHtml,btnPDF,btnCSV,btnOrden,btn,btnCrearInven),state=estado2)
    btnBtnMostrarInven=Button(vtnPrincipal,image=imgBtnMostrarInven,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: ventanaMstInv(lista),state=estado3)
    btnEstaXEstad=Button(vtnPrincipal,image=imgBtnEstaXEstad,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: ventanaEstxEstado(lista),state=estado3)
    btnHtml=Button(vtnPrincipal,image=imgBtnHTML,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: ventanaHTML(lista),state=estado3)
    btnPDF=Button(vtnPrincipal,image=imgBtnPDF,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: ventanaPDF(lista),state=estado3)
    btnCSV=Button(vtnPrincipal,image=imgBtnCSV,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: ventanaCSV(lista),state=estado3)
    btnOrden=Button(vtnPrincipal,image=imgBtnOrden,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: ventanaOrden(lista),state=estado3)

    btn.image_names=imgBtn
    btnCrearInven.image_names=imgBtnCrearInven
    btnBtnMostrarInven.image_names=imgBtnMostrarInven
    btnEstaXEstad.image_names=imgBtnEstaXEstad
    btnHtml.image_names=imgBtnHTML
    btnPDF.image_names=imgBtnPDF
    btnCSV.image_names=imgBtnCSV
    btnOrden.image_names=imgBtnOrden
    lblFondo.image_names=imgFondo

    lblFondo.place(x=-2,y=-2)
    btn.place(x=206, y=235)
    btnCrearInven.place(x=206, y=393)
    btnBtnMostrarInven.place(x=604, y=235)
    btnEstaXEstad.place(x=604, y=393)
    btnHtml.place(x=205, y=547)
    btnPDF.place(x=356, y=547)
    btnCSV.place(x=604, y=547)
    btnOrden.place(x=756, y=547)

global lista, estado1, estado3, estado2

try:
    lista=leer2("laLista")
    estado1=DISABLED
    estado2=DISABLED
    estado3=NORMAL
except:
    try:
        txt=leer("animales.txt")
        lista=[]
        estado1=NORMAL
        estado2=NORMAL
        estado3=DISABLED
    except:        
        lista=[]
        estado1=NORMAL
        estado2=DISABLED
        estado3=DISABLED
configVtnPrincipal(lista,estado1,estado2,estado3)

vtnPrincipal.mainloop()