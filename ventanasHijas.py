from tkinter import *
from funciones import estaXEstado

def ventanaEstxEstado():
    cantidades=estaXEstado()
    vtnEstxEstado= Toplevel()
    vtnEstxEstado.configure(bg="#3C5520")
    vtnEstxEstado.title("Estadistica")
    vtnEstxEstado.geometry("1090x850+0+0")
    vtnEstxEstado.iconbitmap("imagenes/icono.ico")
    vtnEstxEstado.resizable(0,0)

def ventanaMstInv():
    cantidades=estaXEstado()
    vtnEstxEstado= Toplevel()
    vtnEstxEstado.configure(bg="#3C5520")
    vtnEstxEstado.title("Estadistica")
    vtnEstxEstado.geometry("1090x850+0+0")
    vtnEstxEstado.iconbitmap("imagenes/icono.ico")
    vtnEstxEstado.resizable(0,0)