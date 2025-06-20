from tkinter import *
from funciones import *
from ventanasHijas import *

vtnPrincipal=Tk()
def configVtnPrincipal(lista,lista3):
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
    imgBtnHTML=PhotoImage(file="imagenes/btnHTML.png")
    imgBtnPDF=PhotoImage(file="imagenes/btnPDF.png")
    imgBtnCSV=PhotoImage(file="imagenes/btnCSV.png")

    lblFondo=Label(vtnPrincipal,image=imgFondo)
    btn=Button(vtnPrincipal,image=imgBtn,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214")
    btn1=Button(vtnPrincipal,image=imgBtn,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214")
    btn2=Button(vtnPrincipal,image=imgBtn,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: ventanaMstInv(lista3))
    btn3=Button(vtnPrincipal,image=imgBtn,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214")
    btnHtml=Button(vtnPrincipal,image=imgBtnHTML,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=html())
    btnPDF=Button(vtnPrincipal,image=imgBtnPDF,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=pdf(lista))
    btnCSV=Button(vtnPrincipal,image=imgBtnCSV,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: ventanaEstxEstado(lista))

    btn.image_names=imgBtn
    btn1.image_names=imgBtn
    btn2.image_names=imgBtn
    btn3.image_names=imgBtn
    btnHtml.image_names=imgBtnHTML
    btnPDF.image_names=imgBtnPDF
    btnCSV.image_names=imgBtnCSV
    lblFondo.image_names=imgFondo

    lblFondo.place(x=-2,y=-2)
    btn.place(x=206, y=235)
    btn1.place(x=206, y=393)
    btn2.place(x=604, y=235)
    btn3.place(x=604, y=393)
    btnHtml.place(x=205, y=547)
    btnPDF.place(x=356, y=547)
    btnCSV.place(x=756, y=547)

lista3=["https://inaturalist-open-data.s3.amazonaws.com/photos/129658776/original.jpg","https://cdn.britannica.com/22/65322-050-5AA2B60C/Common-wombat.jpg","https://cdn.sanity.io/images/5vm5yn1d/pro/5cb1f9400891d9da5a4926d7814bd1b89127ecba-1300x867.jpg?fm=webp&q=80","https://content.nationalgeographic.com.es/medio/2024/05/31/macho-jin-xi-en-el-zoo-de-madrid_355544e5_240531135148_800x800.jpg"]
lista=leer2("laLista")
configVtnPrincipal(lista,lista3)
vtnPrincipal.mainloop()