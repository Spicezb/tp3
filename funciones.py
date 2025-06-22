from comunicacionApi import *
from clase import *
import pickle
import time
import random
import csv
from fpdf import FPDF
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from tkinter import messagebox

# IMPORTANTE se debe de descargar la libreria fpdf.
indice=0
imagenes=[]
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
    base=open(archivo,"r",encoding="utf-8")
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

def obtenerLista(cant,ventana):
    respuesta = comunicacionGemini(f"Necesito que tomes {cant} nombres comunes de animales, es importante que sean totalmente aleatorios y que no hayas dado en respuestas anteriores, desde wikipedia, un animal por línea. Dame solo los nombres en texo plano, intenta que sea el nombre común pero específico.")
    arch=open("animales.txt","w",encoding="UTF-8")
    arch.write(respuesta)
    arch.close()
    messagebox.showinfo("Obtener lista","La lista fue generada exitosamente !!!")
    ventana.destroy()

def desglozarRespu(respuesta):
    partes=respuesta.split(",")
    nombres=(partes[0],partes[1])
    informacion=partes[2]
    desglose=[nombres,informacion,partes[-1]]
    return(desglose)

def obtener_imagen_wiki(nombre_animal):
    """
    Funcionamiento:
    - Busca en Wikipedia el nombre del animal y devuelve la URL de la imagen principal si existe.
    Entradas:
    - nombre_animal (str): nombre del animal a buscar en Wikipedia.
    Salidas:
    - str: URL directa de imagen (.jpg/.png), o None si no se encontró.
    """
    try:
        # Paso 1: Buscar el título exacto en Wikipedia (en español)
        search_url = "https://es.wikipedia.org/w/api.php"
        search_params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": nombre_animal
        }
        res = requests.get(search_url, params=search_params)
        res.raise_for_status()
        data = res.json()

        if not data["query"]["search"]:
            return None
        
        # Obtener el título del primer resultado
        titulo = data["query"]["search"][0]["title"]

        # Paso 2: Obtener la imagen principal del artículo
        image_params = {
            "action": "query",
            "format": "json",
            "prop": "pageimages",
            "titles": titulo,
            "pithumbsize": 600  # tamaño de la imagen
        }
        img_res = requests.get(search_url, params=image_params)
        img_res.raise_for_status()
        img_data = img_res.json()

        pages = img_data["query"]["pages"]
        for page_id in pages:
            page = pages[page_id]
            if "thumbnail" in page:
                return page["thumbnail"]["source"]

        return None  # No tenía imagen

    except Exception as e:
        print(f"Error al buscar '{nombre_animal}':", e)
        return None

def crearInventario(lista,ventana):
    lista.clear()
    conta=1
    lst=[]
    archivoAnimales=leer("animales.txt")
    lstABuscar=[]
    for i in archivoAnimales:
        i = i.strip()
        if i != "":
            lstABuscar.append(i)
    animalesABusc=random.sample(lstABuscar,20)
    for x in animalesABusc:
        print(x)
        prompt=f"Dame el nombre popular y el científico, que tipo es, Carnivoro, Herbivoro o Omnivoro (RESPONDE SOLAMENTE CON ESAS 3 OPCIONES DE PALABRAS) y una url de una foto"\
                f"de referencia del animal llamado '{x}', saca la informacion de Wikipedia." \
                f"Responde solamente lo que te pedí, sin titulos ni explicaciones, quiero solamente la respuesta directa."
        lst.append(desglozarRespu(comunicacionGemini(prompt)))
        time.sleep(5)
    for x in lst:
        url=obtener_imagen_wiki(x[0][0])
        estado=random.randint(1,5)
        infoAnimal=Animal()
        if conta>10:
            infoAnimal.setId((x[0][0][:1]).lower()+x[0][0][-1]+"0"+str(conta))
        else:
            infoAnimal.setId((x[0][0][:1]).lower()+x[0][0][-1]+str(conta))
        infoAnimal.setNombres(x[0])
        infoAnimal.setURL(url) 
        if x[1][1]!="H":
            peso=round(random.uniform(0, 79), 2)
        else:
            peso=round(random.uniform(80, 100), 2)
        infoAnimal.setInformacion(estado,1,x[1][1],peso)
        conta+=1
        lista.append(infoAnimal)
        print(".")
    grabar(lista,"laLista")
    messagebox.showinfo("Crear Inventario","EL inventario fue generado exitosamente !!!")
    ventana.destroy()
    return lista

def htmlOrden(lista,orden,ventana):
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
            body {{
                background-color: #2D3B2F;
                font-family: 'Rye', cursive;
                font-size: 18px;                          
            }}
            table {{
                width: 85%;
                border-collapse: collapse;
                margin: 20px auto;
            }}
            th, td {{
                border: 1px solid #5A3E1B;
                padding: 10px;
                text-align: center;
            }}
            th {{
                background-color: #3E5637;
                color: white;
            }}
            tr:nth-child(odd) td {{
                background-color: #A3A847;
                color: white;
            }}
            tr:nth-child(even) td {{
                background-color: #F7E9BE;
            }}
            img {{
                width: 100px;
                height: auto;
            }}
            caption {{
                font-size: 1.8em;
                margin: 10px;
                font-weight: bold;
                color: white;
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
    messagebox.showinfo("Generar HTML","HTML generado exitosamente !!!")
    ventana.destroy()


def htmlOrdenAUX(lista,ventana):
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
    htmlOrden(lista,orden,ventana)

def generarCSV(lista,ventana):
    archivoCSV=open("animales.csv",mode="w", newline='',encoding="utf-8-sig")
    reporte=csv.writer(archivoCSV,delimiter=";")
    reporte.writerow(["ID","Nombre común","Nombre científico","Estado","Calificación","Orden","Peso","URL"])
    for i in lista:
        id,(nombreCom,nombreCie),url,[estado,calificacion,orden,peso]=i.getDatos()
        reporte.writerow([id,nombreCom,nombreCie,estado,calificacion,orden,peso,url])
    archivoCSV.close()
    messagebox.showinfo("Generar PDF","PDF generado exitosamente !!!")
    ventana.destroy()

def html(lista,ventana):
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
    lstH.sort(key=lambda peso: peso[3][3], reverse=True)
    lstC.sort(key=lambda peso: peso[3][3], reverse=True)
    lstO.sort(key=lambda peso: peso[3][3], reverse=True)
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
    messagebox.showinfo("Generar HTML","HTML generado exitosamente !!!")
    ventana.destroy()

def reconocerEstados(lista):
    """
    Funcionamiento:
    - Clasifica objetos en un diccionario con claves del 1 al 5, dependiendo del valor en `datos[3][1]`.
    - Si el valor no está en (1, 2, 3), se agrega también datos[3][0] a la tupla.
    Entradas:
    - lista (list): Lista de objetos con el método .getDatos().
    Salidas:
    - estados (dict): Diccionario con claves 1 a 5 y listas de tuplas con datos del objeto.
    """
    estados={1:[],2:[],3:[],4:[],5:[]}
    for i in lista:
        datos=i.getDatos()
        if datos[3][1] not in (1,2,3):
            estados[datos[3][1]].append((datos[0],datos[1][0],datos[3][0]))
        else:
            estados[datos[3][1]].append((datos[0],datos[1][0]))
    return estados

def pdf(lista,ventana):
    """
    Funcionamiento:
    - Genera un reporte en formato PDF con estadísticas organizadas por calificación emocional de los elementos recibidos.
    - Agrupa los datos usando la función reconocerEstados() y los imprime en el PDF bajo títulos como 'Me gusta', 'Favorito', etc.
    - A cada elemento listado se le asigna un número de orden, y se muestra su código y nombre común.
    Entradas:
    - lista (list): Lista de objetos, donde cada objeto debe tener un método .getDatos() que retorna una estructura con la información necesaria.
    Salidas:
    - No retorna ningún valor.
    - Crea un archivo PDF llamado 'reporteCalificacion.pdf' que contiene las estadísticas por calificación.
    """
    conta=1
    contaL=0
    lol=lista
    dicc=reconocerEstados(lol)
    """    for x in dicc:
        for j in dicc[x]:
            print(j[0], j[1])"""
    pdfCalificacion=FPDF()                                     # Se crea el objeto PDF.
    pdfCalificacion.add_page()                                 # Se pone una página.
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
    pdfCalificacion.output('reporteCalificacion.pdf')
    messagebox.showinfo("Generar PDF","PDF generado exitosamente !!!")
    ventana.destroy()

def estaXEstado(lista):
    cantidades=[]
    cont=0
    for x in range(1,6):
        for i in lista:
            lol=i.getDatos()
            if lol[3][0]==x:
                cont+=1
            pass
        cantidades.append((cont,cont*100//20))
        cont=0
    return cantidades

def avanzar(vtn,lista,lista2):
    global indice
    if indice+4<len(lista2):
        indice+=4
        mostrarInventario(vtn,lista2,lista,1,1)

def retroceder(vtn,lista,lista2):
    global indice
    if indice>=4:
        indice-=4
        mostrarInventario(vtn,lista2,lista,1,1)

def calificar(estrellas,cali,indice,ani):
    # e,c,o,p=ani.getInformacion()
    # ani.setInformacion(e,cali,o,p)
    for i,j in enumerate(estrellas[indice]):
        if i<cali-1:
            j.config(text="⭐")
        else:
            j.config(text="☆")

def cargarImagenes(vtn,lista,lista2):
    global imagenes
    imagenes=[]
    imagen=requests.get("https://media.istockphoto.com/id/928418862/es/vector/icono-de-calavera-y-huesos.jpg?s=612x612&w=0&k=20&c=4BTcXgsw_zTLkrf18ZVwol06fZviCwu1T2oDu4-wIaI=")
    imagenPil=Image.open(BytesIO(imagen.content))
    imagenPil=imagenPil.resize((300,250))
    imagenCala=ImageTk.PhotoImage(imagenPil)
    imagen=requests.get("https://static.vecteezy.com/system/resources/previews/029/338/731/non_2x/ambulance-car-illustration-emergency-medical-service-vehicle-isolated-on-white-background-vector.jpg")
    imagenPil=Image.open(BytesIO(imagen.content))
    imagenPil=imagenPil.resize((300,250))
    imagenAmbu=ImageTk.PhotoImage(imagenPil)
    imagen=requests.get("https://static.vecteezy.com/system/resources/previews/026/633/423/non_2x/museum-icon-symbol-design-illustration-vector.jpg")
    imagenPil=Image.open(BytesIO(imagen.content))
    imagenPil=imagenPil.resize((300,250))
    imagenMus=ImageTk.PhotoImage(imagenPil)
    for i,j in enumerate(lista2):
        if lista[i].getInformacion()[0]==5:
            imagenes.append(imagenCala)
        elif lista[i].getInformacion()[0]==4:
            imagenes.append(imagenMus)
        elif lista[i].getInformacion()[0]==2 or lista[i].getInformacion()[0]==3:
            imagenes.append(imagenAmbu)
        else:
            # imagen=requests.get(i.getURL())
            imagen=requests.get(j)
            imagenPil=Image.open(BytesIO(imagen.content))
            imagenPil=imagenPil.resize((300,250))
            imagenTK=ImageTk.PhotoImage(imagenPil)
            imagenes.append(imagenTK)
    vtn.imagenes=imagenes

def mostrarInventario(vtn,lista,lista2,cont,ind):
    global indice
    if cont==0:
        indice=0
        cargarImagenes(vtn,lista2,lista)
    if ind==0:
        indice=0
    btnsEstrellas=[]
    ini=indice
    fin=ini+4
    px=190
    py=20
    ava=tk.Button(vtn,text="-->",command=lambda: avanzar(vtn,lista2,lista))
    ava.place(x=985,y=310)
    retro=tk.Button(vtn,text="<--",command=lambda: retroceder(vtn,lista2,lista))
    retro.place(x=95,y=310)
    for m,i in enumerate(lista[ini:fin]):
        estrellas=[]
        mstImg=tk.Label(vtn,image=imagenes[ini+m])
        mstImg.place(x=px,y=py)
        nombreN,nombreC=lista2[ini+m].getNombres()
        frame=tk.Frame(vtn,width=200,height=25)
        frame.place(x=px+50,y=py+260)
        nombres=tk.Label(frame,text=f"{nombreN}, {nombreC}",anchor="center")
        nombres.place(relx=0.5, rely=0.5, anchor="center") 
        for j in range(2,6):
            estado=lista2[ini+m].getInformacion()[0]
            if (j in (2,3)) or (j==4 and estado in (2,5)) or (j==5 and estado==3):
                boton=tk.Button(vtn,text="☆",width=2,command=lambda cali=j,indice=m,ani=i: calificar(btnsEstrellas,cali,indice,ani))
                boton.place(x=px+93+30*(j-2),y=py+290)
            else:
                boton=tk.Button(vtn,text="☆",width=2)
                boton.place(x=px+93+30*(j-2),y=py+290)
            estrellas.append(boton)
        btnsEstrellas.append(estrellas)
        px+=400
        if px>600:
            px=190
            py+=350

lista=leer2("laLista")
estaXEstado(lista)