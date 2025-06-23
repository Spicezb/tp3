from tkinter import *
from funciones import *
from ventanasHijas import *
import main
cont=0
vtnPrincipal=Tk()
def configVtnPrincipal(lista,lista3):
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
    btn=Button(vtnPrincipal,image=imgBtn,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: vtnBuscar(lista))
    btnCrearInven=Button(vtnPrincipal,image=imgBtnCrearInven,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214",command=lambda: ventanaCrearInven(lista))
    btnBtnMostrarInven=Button(vtnPrincipal,image=imgBtnMostrarInven,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: ventanaMstInv(lista3,lista))
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

#lista3=["https://ca-times.brightspotcdn.com/dims4/default/13b1674/2147483647/strip/true/crop/4262x2842+0+0/resize/1200x800!/quality/75/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2Fef%2F32%2F9feeece34639829007075e2ab4f1%2Fgettyimages-148827046.jpg","https://www.webconsultas.com/sites/default/files/styles/wch_image_schema/public/media/0d/temas/el-caballo-pinto.jpg","https://www.gastroactitud.com/wp-content/uploads/2021/07/frisona-1280x720.jpg","https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Canis_latrans.jpg/250px-Canis_latrans.jpg","https://cdn.sanity.io/images/5vm5yn1d/pro/5cb1f9400891d9da5a4926d7814bd1b89127ecba-1300x867.jpg?fm=webp&q=80","https://fotografias.larazon.es/clipping/cmsimages01/2019/08/26/D2AD4588-59DA-4A71-B8A4-28210E6CCB46/58.jpg?crop=549,311,x60,y0&width=1000&height=567&optimize=low&format=webply","https://greencircleexperience.com/wp-content/uploads/2024/10/Trio-de-Turismo-59.jpg","https://www.muyinteresante.com/wp-content/uploads/sites/5/2023/05/dolphin-7253461_1280-1.jpg"]
lista3=[]
lista=leer2("laLista")
for x in lista:
    lol=x.getURL()
    lista3.append(lol)
configVtnPrincipal(lista,lista3)
vtnPrincipal.mainloop()