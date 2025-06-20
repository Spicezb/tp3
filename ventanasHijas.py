from tkinter import *
from funciones import estaXEstado

def ventanaEstxEstado(lista):
    y=280
    y2=280
    cantidades=estaXEstado(lista)
    vtnEstxEstado= Toplevel()
    vtnEstxEstado.configure(bg="#3C5520")
    vtnEstxEstado.title("Estadistica")
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


def ventanaMstInv():
    cantidades=estaXEstado()
    vtnEstxEstado= Toplevel()
    vtnEstxEstado.configure(bg="#3C5520")
    vtnEstxEstado.title("Estadistica")
    vtnEstxEstado.geometry("1090x850+0+0")
    vtnEstxEstado.iconbitmap("imagenes/icono.ico")
    vtnEstxEstado.resizable(0,0)