from tkinter import *
from funciones import *
from ventanasHijas import *

vtnPrincipal=Tk()
def configVtnPrincipal(lista3):
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
    btn=Button(vtnPrincipal,image=imgBtn,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: vtnBuscar(lista))
    btnCrearInven=Button(vtnPrincipal,image=imgBtnCrearInven,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214",command=lambda: crearInventario(lista))
    btnBtnMostrarInven=Button(vtnPrincipal,image=imgBtnMostrarInven,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: ventanaMstInv(lista3))
    btnEstaXEstad=Button(vtnPrincipal,image=imgBtnEstaXEstad,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: ventanaEstxEstado(lista))
    btnHtml=Button(vtnPrincipal,image=imgBtnHTML,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: ventanaHTML(lista))
    btnPDF=Button(vtnPrincipal,image=imgBtnPDF,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: ventanaPDF(lista))
    btnCSV=Button(vtnPrincipal,image=imgBtnCSV,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: ventanaCSV(lista))
    btnOrden=Button(vtnPrincipal,image=imgBtnOrden,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: ventanaOrden(lista))

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

lista3=["https://inaturalist-open-data.s3.amazonaws.com/photos/129658776/original.jpg","https://cdn.britannica.com/22/65322-050-5AA2B60C/Common-wombat.jpg","https://cdn.sanity.io/images/5vm5yn1d/pro/5cb1f9400891d9da5a4926d7814bd1b89127ecba-1300x867.jpg?fm=webp&q=80","https://content.nationalgeographic.com.es/medio/2024/05/31/macho-jin-xi-en-el-zoo-de-madrid_355544e5_240531135148_800x800.jpg"]
global lista
lista=leer2("laLista")
configVtnPrincipal(lista3)
vtnPrincipal.mainloop()