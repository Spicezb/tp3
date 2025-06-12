from comunicacionApi import *

def obtenerLista():
    cant = int(input("Ingrese la cantidad de animales que desea buscar: "))
    respuesta = comunicacionGemini(f"Necesito que tomes {cant} nombres comunes de animales, es importante que sean totalmente aleatorios y que no hayas dado en respuestas anteriores, desde wikipedia, un animal por línea. Dame solo los nombres en texo plano, intenta que sea el nombre común pero específico.")
    arch=open("animales.txt","w",encoding="UTF-8")
    arch.write(respuesta)
    arch.close()
    return print("Los animales fueron agregados.")

obtenerLista()