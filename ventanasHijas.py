from tkinter import *
from funciones import *

def ventanaEstxEstado():
    cantidades=estaXEstado()
    vtnEstxEstado= Toplevel()
    vtnEstxEstado.configure(bg="#3C5520")
    vtnEstxEstado.title("Estadistica")
    vtnEstxEstado.geometry("1090x850+0+0")
    vtnEstxEstado.iconbitmap("imagenes/icono.ico")
    vtnEstxEstado.resizable(0,0)

def ventanaMstInv(lista):
    vtnMstInv= Toplevel()
    vtnMstInv.configure(bg="#3C5520")
    vtnMstInv.title("Inventario")
    vtnMstInv.geometry("1090x850+0+0")
    vtnMstInv.iconbitmap("imagenes/icono.ico")
    vtnMstInv.resizable(0,0)
    mostrarInventario(vtnMstInv,lista)