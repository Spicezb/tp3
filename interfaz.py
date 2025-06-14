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
    vtnPrincipal.state("zoomed")
    vtnPrincipal.configure(bg="#3C5520")
    vtnPrincipal.title("Zoo Inventario")
    vtnPrincipal.iconbitmap("imagenes/icono.ico")
    imgBtn=PhotoImage(file="imagenes/plantillaBotones.png")
    btn=Button(vtnPrincipal,image=imgBtn,borderwidth=0, highlightthickness=0,bg="#3C5520",activebackground="#3C5520")
    btn.image_names=imgBtn
    btn1=Button(vtnPrincipal,image=imgBtn,borderwidth=0, highlightthickness=0,bg="#3C5520",activebackground="#3C5520")
    btn1.image_names=imgBtn
    btn2=Button(vtnPrincipal,image=imgBtn,borderwidth=0, highlightthickness=0,bg="#3C5520",activebackground="#3C5520")
    btn2.image_names=imgBtn
    btn3=Button(vtnPrincipal,image=imgBtn,borderwidth=0, highlightthickness=0,bg="#3C5520",activebackground="#3C5520")
    btn3.image_names=imgBtn
    btn.place(x=100, y=200)
    btn1.place(x=100, y=400)
    btn2.place(x=600, y=200)
    btn3.place(x=600, y=400)

configVtnPrincipal()
vtnPrincipal.mainloop()