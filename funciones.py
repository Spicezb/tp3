from comunicacionApi import *
from clase import *
import pickle
import time
import random
import csv
from fpdf import FPDF
# IMPORTANTE se debe de descargar la libreria fpdf.

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
        print(".")
        i = i.strip()
        if i != "":
            print(".")
            prompt=f"Dame el nombre popular y el científico, que tipo es, Carnivoro, Herbivoro o Omnivoro (RESPONDE SOLAMENTE CON ESAS 3 OPCIONES DE PALABRAS) y una url de una foto"\
                    f"de referencia del animal llamado '{i}', saca la informacion de Wikipedia." \
                    f"Responde solamente lo que te pedí, sin titulos ni explicaciones, quiero solamente la respuesta directa."
            print(comunicacionGemini(prompt))
            lst.append(desglozarRespu(comunicacionGemini(prompt)))
            print(".")
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
        print(".")
    grabar(lstAnimal,"laLista")

def htmlOrden(lista,orden):
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
    lista=leer2("laLista")
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


def html():
    """
    Funcionamiento:
    - Genera un archivo HTML con una tabla que categoriza animales en tres grupos: carnívoros, herbívoros y omnívoros.
    - Extrae datos desde un archivo o fuente mediante la función `leer2("laLista")`, organiza los animales según su tipo, y los muestra en una tabla estilizada.

    Entradas:
    - No recibe parámetros directamente. Utiliza internamente la función `leer2("laLista")` para obtener la lista de objetos.

    Salidas:
    - No retorna ningún valor.
    - Crea un archivo llamado "Reporte.html" con una tabla que presenta el orden (carnívoro, herbívoro u omnívoro), el peso y el nombre común de los animales.
    """
    lista=leer2("laLista")
    lstH=[]
    lstC=[]
    lstO=[]
    contC=0
    contH=0
    contO=0
    conta=0
    for i in lista:
        datos=i.getDatos()
        if datos[3][2] == "C":
            lstC.append(datos)
            contC+=1
        elif datos[3][2] == "H":
            lstH.append(datos)
            contH+=1
        else:
            lstO.append(datos)
            contO+=1
    html="""
    <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabla de animales</title>
    <style>
        body {
                background-color: #2D3B2F;
                font-family: 'Rye', cursive;
                font-size: 18px;                          
        }
        table {
                width: 85%;
                border-collapse: collapse;
                margin: 20px auto;
            }
            th, td {
                border: 1px solid #5A3E1B;
                padding: 10px;
                text-align: center;
            }
            th {
                background-color: #3E5637;
                color: white;
                font-size: 28px;
            }
            tr:nth-child(odd) td {
                background-color: #A3A847;
                color: white
            }
            tr:nth-child(even) td {
                background-color: #F7E9BE;
                color: black
            }
    </style>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>Orden</th>
                <th>Peso</th>
                <th>Nombre común</th>
            </tr>
        </thead>
        <tbody>"""
    for x in lstH:
        if conta==0:
            html+=f"""
                <tr>
                <td rowspan="{contH}">Herbívoros</td>
                <td>{x[3][3]}</td>
                <td>{x[1][0]}</td>
                </tr>"""
            conta+=1
        else:
            html+=f"""
                <tr>
                <td>{x[3][3]}</td>
                <td>{x[1][0]}</td>
                </tr>"""
    conta=0
    for x in lstC:
        if conta==0:
            html+=f"""
                <tr>
                <td rowspan="{contC}">Carnivoros</td>
                <td>{x[3][3]}</td>
                <td>{x[1][0]}</td>
                </tr>"""
            conta+=1
        else:
            html+=f"""
                <tr>
                <td>{x[3][3]}</td>
                <td>{x[1][0]}</td>
                </tr>"""
    conta=0
    for x in lstO:
        if conta==0:
            html+=f"""
            </tr>
            <tr>
            <td rowspan="{contO}">Omnivoros</td>
            <td>{x[3][3]}</td>
            <td>{x[1][0]}</td>
            </tr>"""
            conta+=1
        else:
            html+=f"""
                <tr>
                <td>{x[3][3]}</td>
                <td>{x[1][0]}</td>
                </tr>"""            
    html+="""
        </tbody>
    </table>
</body>
</html>
    """
    arch=open("Reporte.html", "w", encoding="utf-8")
    arch.write(html)
    arch.close()

def reconocerEstados(lista):
    estados={1:[],2:[],3:[],4:[],5:[]}
    for i in lista:
        datos=i.getDatos()
        if datos[3][1] not in (1,2,3):
            estados[datos[3][1]].append((datos[0],datos[1][0],datos[3][0]))
        else:
            estados[datos[3][1]].append((datos[0],datos[1][0]))
    return estados

def pdf(lista):
    conta=1
    contaL=0
    dicc= reconocerEstados(lista)
    """    for x in dicc:
        for j in dicc[x]:
            print(j[0], j[1])"""
    pdfCalificacion=FPDF()                                # Se crea el objeto PDF.
    pdfCalificacion.add_page()                             # Se pone una página.
    pdfCalificacion.set_font("helvetica", "B", 16)             # Se le da formato a las letras.
    pdfCalificacion.cell(0, 10, "Estadisticas por Calificación", align="C")
    pdfCalificacion.ln(5)
    for x in dicc:
        pdfCalificacion.ln(10)
        pdfCalificacion.set_font('helvetica', 'B', 14)
        if conta==1:
            pdfCalificacion.cell(0, 10, 'No marcado', align='L')
            conta+=1
        elif conta==2:
            pdfCalificacion.cell(0, 10, 'Me Gusta', align='L')
            conta+=1
        elif conta==3:
            pdfCalificacion.cell(0, 10, 'Favorito', align='L')
            conta+=1
        elif conta==4:
            pdfCalificacion.cell(0, 10, 'Me entristese', align='L')
            conta+=1
        else:
            pdfCalificacion.cell(0, 10, 'Me enoja', align='L')
            conta+=1
        pdfCalificacion.ln(5)
        pdfCalificacion.set_font('helvetica', '', 12)
        pdfCalificacion.cell(0, 10, "       Código      Nombre Común",align='L')    
        for j in dicc[x]:
            contaL+=1
            pdfCalificacion.ln(5)
            pdfCalificacion.set_font('helvetica', '', 12)
            pdfCalificacion.cell(0, 10, f"{contaL}.       {j[0]}          {j[1]}",align='L')
        contaL=0
    pdfCalificacion.output('reporteAplazados.pdf')

lista=leer2("laLista")

pdf(lista)