from comunicacionApi import *
import pickle
import time
#Definición de funciones
def leer(archivo):
    """
    Funcionamiento:
    - Lee el diccionario con la informacion de los pokemones que se encuentra en el archivo.
    Entradas: 
    - archivo(str): Es el archivo que contiene el diccionario con la información de los pokemones.
    Salidas:
    - Retorna el diccionario.
    """
    base=open(archivo,"r")
    dicc=base.readlines()
    base.close()
    return dicc

def grabar(dicc,archivo):
    """
    Funcionamiento:
    - Graba el diccionario actualizado en el archivo.
    Entradas:
    - dicc(dict): Es el diccionario a grabar.
    - archivo(str): Es el archivo que contiene el diccionario con la información de los pokemones.
    Salidas:
    - Graba el diccionario en el archivo y retorna un string vacío.
    """
    base=open(archivo,"w")
    pickle.dump(dicc,base)
    base.close()
    return ""

def obtenerLista():
    cant=int(input("Ingrese la cantidad de animales que desea buscar: "))
    respuesta = comunicacionGemini(f"Necesito que tomes {cant} nombres comunes de animales, es importante que sean totalmente aleatorios y que no hayas dado en respuestas anteriores, desde wikipedia, un animal por línea. Dame solo los nombres en texo plano, intenta que sea el nombre común pero específico.")
    arch=open("animales.txt","w",encoding="UTF-8")
    arch.write(respuesta)
    arch.close()
    return print("Los animales fueron agregados.")

def desglozarRespu(respuesta):
    # Separar por punto y coma
    partes=respuesta.split(",")
    nombres=(partes[0],partes[1][2:-1])
    informacion=partes[2:-1]
    desglose=[nombres,informacion,partes[-1][1:-1]]
    return(desglose)

def crearInventario():
    animal=[]
    lst=[]
    archivoAnimales=leer("animales.txt")
    for i in archivoAnimales:
        i = i.strip()
        if i != "":
            prompt=f"Dame el nombre popular y el científico, hábitat, dieta y una url de una foto de referencia del animal llamado '{i}', saca la informacion de Wikipedia." \
                    "Responde solamente lo que te pedí, sin titulos ni explicaciones, quiero solamente la respuesta directa. no pngas ** entre nombres ni hagas '\ n' al final"
            respuesta=comunicacionGemini(prompt)
            desglose=desglozarRespu(respuesta)
            animal.append(desglose)
            lst.append(animal)
            time.sleep(5)
            animal=[]
    print(lst)
crearInventario()