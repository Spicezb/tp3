from tkinter import *
from funciones import *

def ventanaEstxEstado(lista):
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

def ventanaHTML():
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
    lblTitulo=Label(vtnHTML,text="¿Desea generar un HTML con las\n estadiscas de los animales?",bg="#193214",fg="#f7c760",font=("Fixedsys", 18))
    btnCancelar=Button(vtnHTML,image=imgBtnCancelar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: vtnHTML.destroy())
    btnAceptar=Button(vtnHTML,image=imgBtnAceptar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: html(vtnHTML))
    lblFondo.image_names=imgHTML
    btnCancelar.image_names=imgBtnCancelar
    btnAceptar.image_names=imgBtnAceptar
    lblFondo.place(x=-2,y=-2)
    lblTitulo.place(x=150,y=120)
    btnCancelar.place(x=450,y=250)
    btnAceptar.place(x=150,y=250)

def ventanaPDF(lista):
    vtnPDF = Toplevel()
    vtnPDF.title("Generar HTML")
    vtnPDF.geometry("794x445")
    vtnPDF.configure(bg="#3C5520")
    vtnPDF.iconbitmap("imagenes/icono.ico")
    vtnPDF.resizable(0,0)
    imgHTML=PhotoImage(file="imagenes/fondoHTML.png")
    imgBtnCancelar=PhotoImage(file="imagenes/btnCancelar.png")
    imgBtnAceptar=PhotoImage(file="imagenes/btnAceptar.png")
    lblFondo=Label(vtnPDF,image=imgHTML)
    lblTitulo=Label(vtnPDF,text="¿Desea generar un PDF con las\n estadiscas de los animales?",bg="#193214",fg="#f7c760",font=("Fixedsys", 17))
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
    vtnCSV = Toplevel()
    vtnCSV.title("Generar CSV")
    vtnCSV.geometry("794x445")
    vtnCSV.configure(bg="#3C5520")
    vtnCSV.iconbitmap("imagenes/icono.ico")
    vtnCSV.resizable(0,0)
    imgHTML=PhotoImage(file="imagenes/fondoHTML.png")
    imgBtnCancelar=PhotoImage(file="imagenes/btnCancelar.png")
    imgBtnAceptar=PhotoImage(file="imagenes/btnAceptar.png")
    lblFondo=Label(vtnCSV,image=imgHTML)
    lblTitulo=Label(vtnCSV,text="¿Desea generar un PDF con las\n estadiscas de los animales?",bg="#193214",fg="#f7c760",font=("Fixedsys", 17))
    btnCancelar=Button(vtnCSV,image=imgBtnCancelar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: vtnCSV.destroy())
    btnAceptar=Button(vtnCSV,image=imgBtnAceptar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: generarCSV(lista,vtnCSV))
    lblFondo.image_names=imgHTML
    btnCancelar.image_names=imgBtnCancelar
    btnAceptar.image_names=imgBtnAceptar
    lblFondo.place(x=-2,y=-2)
    lblTitulo.place(x=150,y=120)
    btnCancelar.place(x=450,y=250)
    btnAceptar.place(x=150,y=250)

def ventanaMstInv(lista):
    vtnMstInv= Toplevel()
    vtnMstInv.configure(bg="#3C5520")
    vtnMstInv.title("Inventario")
    vtnMstInv.geometry("1090x850+0+0")
    vtnMstInv.iconbitmap("imagenes/icono.ico")
    vtnMstInv.resizable(0,0)
    mostrarInventario(vtnMstInv,lista)

def ventanaOrden(lista):
    vtnOrden = Toplevel()
    vtnOrden.title("Generar CSV")
    vtnOrden.geometry("794x445")
    vtnOrden.configure(bg="#3C5520")
    vtnOrden.iconbitmap("imagenes/icono.ico")
    vtnOrden.resizable(0,0)
    imgHTML=PhotoImage(file="imagenes/fondoHTML.png")
    imgBtnCancelar=PhotoImage(file="imagenes/btnCancelar.png")
    imgBtnAceptar=PhotoImage(file="imagenes/btnAceptar.png")
    lblFondo=Label(vtnOrden,image=imgHTML)
    lblTitulo=Label(vtnOrden,text="¿Desea generar un PDF con las\n estadiscas de los animales?",bg="#193214",fg="#f7c760",font=("Fixedsys", 17))
    btnCancelar=Button(vtnOrden,image=imgBtnCancelar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: vtnOrden.destroy())
    btnAceptar=Button(vtnOrden,image=imgBtnAceptar,borderwidth=0, highlightthickness=0,bg="#193214",activebackground="#193214", command=lambda: htmlOrdenAUX(lista,vtnOrden))
    lblFondo.image_names=imgHTML
    btnCancelar.image_names=imgBtnCancelar
    btnAceptar.image_names=imgBtnAceptar
    lblFondo.place(x=-2,y=-2)
    lblTitulo.place(x=150,y=120)
    btnCancelar.place(x=450,y=250)
    btnAceptar.place(x=150,y=250)