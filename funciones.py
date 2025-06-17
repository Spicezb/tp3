from comunicacionApi import *
from clase import *
import pickle
import time
import random
import csv

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

def leer2(archivo):
    """
    Funcionamiento:
    - Lee el diccionario con la informacion de los pokemones que se encuentra en el archivo.
    Entradas: 
    - archivo(str): Es el archivo que contiene el diccionario con la información de los pokemones.
    Salidas:
    - Retorna el diccionario.
    """
    base=open(archivo,"rb")
    dicc=pickle.load(base)
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

def htmlOrden (lista,orden):
    """
    Entradas:
    - lista(list): Lista de objetos.
    - orden(tuple): Tupla que contiene la palabra del orden y la letra.
    """
    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Animales {orden[0]}</title>
        <style>
            table {{
                width: 85%;
                border-collapse: collapse;
                margin: 20px auto;
            }}
            th, td {{
                border: 1px solid #666;
                padding: 10px;
                text-align: center;
            }}
            th {{
                background-color: #004080;
                color: white;
            }}
            tr:nth-child(odd) td {{
                background-color: #e6f0ff;
            }}
            tr:nth-child(even) td {{
                background-color: #ffffff;
            }}
            img {{
                width: 100px;
                height: auto;
            }}
            caption {{
                font-size: 1.8em;
                margin: 10px;
                font-weight: bold;
                color: #004080;
            }}
        </style>
    </head>
    <body>
        <table>
            <caption>Animales {orden[0]}</caption>
            <thead>
                <tr>
                    <th>#</th>
                    <th>Código</th>
                    <th>Nombre común</th>
                    <th>Nombre científico</th>
                    <th>Imagen</th>
                </tr>
            </thead>
            <tbody>
    """
    for i,animal in enumerate(lista):
        datos=animal.getDatos()
        if datos[3][2]!=orden[1]:
            continue
        id,nombre,nombreC,url=datos[0],datos[1][0],datos[1][1],datos[2]
        print(url)
        html += f"""
                <tr>
                    <td>{i+1}</td>
                    <td>{id}</td>
                    <td>{nombre}</td>
                    <td><i>{nombreC}</i></td>
                    <td><img src="{url}" alt="{nombre}"></td>
                </tr>
        """
    html += """
            </tbody>
        </table>
    </body>
    </html>
    """
    arch = open("animalesPorOrden.html", "w", encoding="utf-8")
    arch.write(html)
    arch.close()

def htmlOrdenAUX():
    lista = leer2("laLista")
    while True:
        try:
            opcion = input("\nIngrese la opción que desea.\n" \
            "1) Carnívoros\n" \
            "2) Herbívoros\n" \
            "3) Omnívoros\n" \
            "Opción: ")
            if opcion not in ("1","2","3"):
                raise ValueError
            break
        except ValueError:
            print("Debe seleccionar una de las opciones anteriores.")
    if opcion == "1":
        orden = ("Carnívoros","C")
    elif opcion == "2":
        orden = ("Herbívoros","H")
    else:
        orden = ("Omnívoros","O")
    htmlOrden(lista,orden)

def generarCSV():
    lista = leer2("laLista")
    archivoCSV=open("animales.csv",mode="w", newline='',encoding="utf-8-sig")
    reporte=csv.writer(archivoCSV,delimiter=",")
    reporte.writerow(["ID","Nombre común","Nombre científico","Estado","Calificación","Orden","Peso","URL"])
    for i in lista:
        id,(nombreCom,nombreCie),url,[estado,calificacion,orden,peso]=i.getDatos()
        reporte.writerow([id,nombreCom,nombreCie,estado,calificacion,orden,peso,url])
    archivoCSV.close()
    print("El reporte .CSV ha sido creado.")