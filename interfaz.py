from tkinter import *

vtnPrincipal=Tk()
def configVtnPrincipal():
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

    lblFondo=Label(vtnPrincipal,image=imgFondo)
    btn=Button(vtnPrincipal,image=imgBtn,borderwidth=0, highlightthickness=0,bg="#3C5520",activebackground="#3C5520")
    btn1=Button(vtnPrincipal,image=imgBtn,borderwidth=0, highlightthickness=0,bg="#3C5520",activebackground="#3C5520")
    btn2=Button(vtnPrincipal,image=imgBtn,borderwidth=0, highlightthickness=0,bg="#3C5520",activebackground="#3C5520")
    btn3=Button(vtnPrincipal,image=imgBtn,borderwidth=0, highlightthickness=0,bg="#3C5520",activebackground="#3C5520")
    btn.image_names=imgBtn
    btn1.image_names=imgBtn
    btn2.image_names=imgBtn
    btn3.image_names=imgBtn
    lblFondo.image_names=imgFondo
    lblFondo.place(x=-2,y=-2)
    btn.place(x=206, y=235)
    btn1.place(x=206, y=393)
    btn2.place(x=604, y=235)
    btn3.place(x=604, y=393)


configVtnPrincipal()
vtnPrincipal.mainloop()