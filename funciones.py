from comunicacionApi import *
from clase import *
import pickle
import time
import random

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
    base=open(archivo,"wb")
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
    partes=respuesta.split(",")
    nombres=(partes[0],partes[1])
    informacion=partes[2]
    desglose=[nombres,informacion,partes[-1]]
    return(desglose)

def crearInventario():
    conta=1
    lstAnimal=[]
    lst=[]
    archivoAnimales=leer("animales.txt")
    for i in archivoAnimales:
        i = i.strip()
        if i != "":
            prompt=f"Dame el nombre popular y el científico, que tipo es, Carnivoro, Herbivoro o Omnivoro (RESPONDE SOLAMENTE CON ESAS 3 OPCIONES DE PALABRAS) y una url de una foto"\
                    f"de referencia del animal llamado '{i}', saca la informacion de Wikipedia." \
                    f"Responde solamente lo que te pedí, sin titulos ni explicaciones, quiero solamente la respuesta directa."
            lst.append(desglozarRespu(comunicacionGemini(prompt)))
            time.sleep(5)
    for x in lst:
        estado=random.randint(1,5)
        calificacion=int(input("1) No marcado\n2) Me gusta\n3)Favorito\n4) Me entristece\n5) Me enoja"))
        infoAnimal=Animal()
        if conta>10:
            infoAnimal.setId((x[0][0][:1]).lower()+x[0][0][-1]+"0"+str(conta))
        else:
            infoAnimal.setId((x[0][0][:1]).lower()+x[0][0][-1]+str(conta))
        infoAnimal.setNombres(x[0])
        infoAnimal.setURL(x[-1])
        infoAnimal.setInformacion(estado,calificacion,x[1][1],78)
        conta+=1
        lstAnimal.append(infoAnimal)
    grabar(lstAnimal,"laLista")
    print(lstAnimal)

crearInventario()