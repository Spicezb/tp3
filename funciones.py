# Realizado Por Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado
# Fecha de inicio: 
# Última modificación:
# Versión de Python 3.13.2

# Importaciones de Librerías
from comunicacionApi import *
from clase import *
import pickle
import time
import random
import csv
from fpdf import FPDF
from tkinter import *
from PIL import Image, ImageTk, UnidentifiedImageError
import requests
from io import BytesIO
from tkinter import messagebox
import re

# IMPORTANTE se debe de descargar la libreria fpdf.
# IMPORTANTE se debe de descargar la libreria pillow.
# IMPORTANTE se debe de descargar la libreria google-generativeai.

indice=0
imagenes=[]

#Definición de funciones
def leer(archivo):
    """
    Funcionamiento:
    - Lee las lineas del archivo txt.
    Entradas: 
    - archivo(str): Es el archivo txt que contiene los nombres de los animales.
    Salidas:
    - Retorna las lineas.
    """
    base=open(archivo,"r",encoding="utf-8")
    lineas=base.readlines()
    base.close()
    return lineas

def leer2(archivo):
    """
    Funcionamiento:
    - Lee la lista de la base de datos de los animales.
    Entradas: 
    - archivo(str): Es el archivo que contiene la lista de objetos..
    Salidas:
    - Retorna la lista
    """
    base=open(archivo,"rb")
    lista=pickle.load(base)
    base.close()
    return lista

def grabar(dicc,archivo):
    """
    Funcionamiento:
    - Graba la lista actualizada en el archivo.
    Entradas:
    - dicc(list): Es la lista a grabar.
    - archivo(str): Es el archivo en donde se guarda.
    Salidas:
    - Graba la lista en el archivo.
    """
    base=open(archivo,"wb")
    pickle.dump(dicc,base)
    base.close()
    return ""

def obtenerLista(cant,ventana):
    """
    Funcionamiento:
    - Verifica que el valor ingresado sea un número entero mayor o igual a 20.
    - Si no cumple con esa condición, muestra un mensaje de error y vuelve a mostrar la ventana.
    - Si la validación es exitosa, realiza una consulta a la IA (Gemini) para obtener una lista con la cantidad especificada de nombres comunes de animales desde Wikipedia.
    - Guarda la lista en un archivo de texto plano llamado "animales.txt".
    - Muestra un mensaje de éxito y cierra la ventana actual.
    Entradas:
    - cant(str): Cadena que representa la cantidad de animales que se desea obtener. Debe ser un número entero >= 20.
    - ventana(tkinter.Toplevel): Ventana desde la cual se ejecuta la función. Se destruye si todo sale bien, o se vuelve a mostrar si hay error.
    Salidas: 
    - Crea el archivo "animales.txt" con los nombres generados.
    - Muestra mensajes informativos o de error mediante `messagebox`.
    """
    try:
        if not re.match(r"^[0-9]{1,}$", cant):
            raise TypeError
        elif int(cant)<20:
            raise TypeError
    except TypeError:
        messagebox.showerror("Error","La cantidad debe de ser un número entero mayor o igual a 20.")
        return ventana.deiconify()
    respuesta = comunicacionGemini(f"Necesito que tomes exactamente {cant} nombres comunes de animales, es importante que sean totalmente aleatorios y que no hayas dado en respuestas anteriores, desde wikipedia, un animal por línea. Dame solo los nombres en texo plano, intenta que sea el nombre común pero específico.")
    arch=open("animales.txt","w",encoding="UTF-8")
    arch.write(respuesta)
    arch.close()
    messagebox.showinfo("Obtener lista","La lista fue generada exitosamente !!!")
    ventana.destroy()

def desglozarRespu(respuesta):
    """
    Funcionamiento:
    - Descompone una cadena de texto separada por comas en partes específicas.
    - Agrupa el primer y segundo elemento como una tupla (nombres comunes y científicos).
    - Devuelve una lista estructurada con esos tres componentes.
    Entradas:
    - respuesta(str): Cadena de texto con varios elementos separados por comas. 
    - Se espera que al menos tenga 4 elementos.
    Salidas:
    - list: Lista con tres elementos:
        1. Tupla con los dos primeros elementos de la cadena.
        2. El tercer elemento como cadena.
        3. El último elemento de la cadena.
    """
    partes=respuesta.split(",")
    nombres=(partes[0],partes[1])
    informacion=partes[2]
    desglose=[nombres,informacion,partes[-1]]
    return(desglose)

def buscarImagen(animal):
    """
    Se negocio con la profe Laura el día 23/06/2025, para utilizar directamente el API de wikimedia, para poder evitar
    el problema, de que las imagenes que envía gemini no sirven, por eso usar esta directamente para evitar el problema.
    si llegara haber un error con estas, solamente se le pone una imagen de imagen not found por defecto.
    Se investigó como se usaba la API y cuales eran los parametros para obtener esta información.
    Funcionamiento:
    - Realiza una búsqueda en la API de Wikipedia para encontrar la página relacionada con el nombre de un animal dado.
    - Luego, consulta si esa página tiene una imagen asociada.
    - Si encuentra una imagen, retorna la URL directa de esa imagen.
    Entradas:
    - anima(str): Nombre común del animal a buscar.
    Salidas:
    - str: URL de la imagen miniatura asociada al animal si se encuentra.
    - None: Si no se encuentra ninguna imagen.
    """
    buscarEnAPI="https://es.wikipedia.org/w/api.php"
    parametrosABuscar={"action": "query","format": "json","list": "search","srsearch": animal}
    respuesta=requests.get(buscarEnAPI, params=parametrosABuscar)
    respuesta.raise_for_status()
    data=respuesta.json()

    animalBuscar=data["query"]["search"][0]["title"]
    parametrosImagen={"action":"query","format":"json","prop":"pageimages","titles":animalBuscar}

    respuestaImagen=requests.get(buscarEnAPI, params=parametrosImagen)
    respuestaImagen.raise_for_status()
    imagenInfo=respuestaImagen.json()

    info=imagenInfo["query"]["pages"]
    for i in info:
        page=info[i]
        if "thumbnail" in page:
            return page["thumbnail"]["source"]

def verificarImagen(url):
    """
    Funcionamiento:
    - Verifica si una URL dada apunta a una imagen válida y accesible.
    - Realiza una solicitud HTTP a la URL y comprueba si el contenido es una imagen y si se obtuvo correctamente.
    Entradas:
    - url (str): URL que se desea verificar.
    Salidas:
    - bool: 
        - True si la URL es válida, responde con código 200 y contiene una imagen.
        - False si ocurre un error en la solicitud o el contenido no es una imagen.
    """
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200 and "image" in r.headers.get("Content-Type", ""):
            return True
    except (requests.exceptions.RequestException, UnidentifiedImageError) as e:
        return False

def crearInventario(lista,ventana):
    """
    Funcionamiento:
    - Genera un inventario aleatorio de 20 animales usando nombres tomados del archivo de texto(animales.txt).
    - Por cada animal seleccionado, consulta a la IA (Gemini) para obtener:
        - Nombre común y científico.
        - Tipo (carnívoro, herbívoro u omnívoro).
        - URL referencial desde Wikipedia.
    - Valida la URL de la imagen; si no sirve, se le asigna una imagen por defecto.
    - Asigna valores como ID, nombres, tipo, estado y peso al objeto `Animal`.
    - Guarda la lista resultante en un archivo.
    Entradas:
    - lista (list):Lista original(se vacía y se llena con los nuevos objetos `Animal`).
    - ventana(tk.Toplevel): Ventana desde la cual se llama la función. Se destruye al finalizar.
    Salidas:
    - list: Lista actualizada con 20 objetos `Animal` generados.
    """
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
                f"Responde solamente lo que te pedí, sin titulos ni explicaciones, quiero solamente la respuesta directa y en texto plano."
        lst.append(desglozarRespu(comunicacionGemini(prompt)))
        time.sleep(5)
    for x in lst:
        infoAnimal=Animal()
        url=buscarImagen(x[0][0])
        verificar=verificarImagen(url)
        if verificar==True:
            estado=1
            infoAnimal.setURL(url)
        else:
            infoAnimal.setURL("https://static.vecteezy.com/system/resources/previews/022/059/000/non_2x/no-image-available-icon-vector.jpg")
            estado=random.randint(2,5)
        if conta>10:
            infoAnimal.setId((x[0][0][:1]).lower()+x[0][0][-1]+"0"+str(conta))
        else:
            infoAnimal.setId((x[0][0][:1]).lower()+x[0][0][-1]+str(conta))
        infoAnimal.setNombres(x[0])
        if x[1][1]!="H":
            peso=round(random.uniform(0, 79), 2)
        else:
            peso=round(random.uniform(80, 100), 2)
        infoAnimal.setInformacion(estado,1,x[1][1].lower(),peso)
        conta+=1
        lista.append(infoAnimal)
        print(".")
    grabar(lista,"laLista")
    messagebox.showinfo("Crear Inventario","EL inventario fue generado exitosamente !!!")
    ventana.destroy()
    return lista

def htmlOrden(lista,orden,ventana):
    """
    Funcionamiento:
    - Crea el reporte html de los animales según su orden (carnívoros, herbívoros u omnívoros)
    Entradas:
    - lista(list): Lista de objetos.
    - orden(tuple): Tupla que contiene la palabra del orden y la letra.
    - ventana: Es la ventana donde se muestra la funcionalidad.
    Salidas:
    - Genera el archivo html con la información.
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

def htmlOrdenAUX(opcion, lista,ventana):
    """
    Funcionamiento:
    - Verifica que el usuario haya seleccionado una opción válida para ordenar animales por tipo.
    - Traduce la opción textual (Carnívoros, Herbívoros, Omnívoros) a una tupla que contiene:
        1. El nombre completo del tipo.
        2. Su abreviatura (C, H, O).
    - Llama a la función `htmlOrden` para generar el HTML correspondiente al tipo elegido.
    - Si no se selecciona ninguna opción, muestra un mensaje de error y vuelve a mostrar la ventana.
    Entradas:
    - opcion(str): Texto de la opción seleccionada ("Carnívoros", "Herbívoros" u "Omnívoros").
    - lista(list): Lista de objetos `Animal` que se desea ordenar y filtrar.
    - ventana(Toplevel): Ventana desde la cual se ejecuta la función, y que puede cerrarse o volver a mostrarse según el caso.
    Salidas:
    - No retorna ningún valor.
    - Llama a `htmlOrden` con la tupla correspondiente para generar la salida HTML.
    """
    if opcion == "":
        messagebox.showerror("Error","Debe de elegir un orden.")
        return ventana.deiconify()
    elif opcion == "Carnívoros":
        orden = ("Carnívoros","c")
    elif opcion == "Herbívoros":
        orden = ("Herbívoros","h")
    else:
        orden = ("Omnívoros","o")
    htmlOrden(lista,orden,ventana)

def generarCSV(lista,ventana):
    """
    Funcionamiento:
    - Genera un archivo CSV llamado "animales.csv" con la información de cada objeto `Animal` presente en la lista.
    - Escribe los encabezados correspondientes y luego exporta los datos organizados en filas.
    - Muestra un mensaje de éxito cuando finaliza y cierra la ventana desde la cual se ejecutó.
    Entradas:
    - lista(list): Lista de objetos `Animal`, de los cuales se extrae la información con el método `getDatos()`.
    - ventana(Toplevel): Ventana activa que se destruye tras completar la exportación.
    Salidas:
    - Crea un archivo llamado "animales.csv" con los datos de los animales en formato separado por comas (CSV).
    """
    archivoCSV=open("animales.csv",mode="w", newline='',encoding="utf-8-sig")
    reporte=csv.writer(archivoCSV,delimiter=",")
    reporte.writerow(["ID","Nombre común","Nombre científico","Estado","Calificación","Orden","Peso","URL"])
    for i in lista:
        id,(nombreCom,nombreCie),url,[estado,calificacion,orden,peso]=i.getDatos()
        reporte.writerow([id,nombreCom,nombreCie,estado,calificacion,orden,peso,url])
    archivoCSV.close()
    messagebox.showinfo("Generar CSV","CSV generado exitosamente !!!")
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
    """
    Funcionamiento:
    - Recorre la lista de objetos `Animal` y cuenta cuántos hay en cada uno de los 5 posibles estados (del 1 al 5).
    - Por cada estado, calcula la cantidad total y el porcentaje que representa respecto al total (se asume que la lista tiene 20 animales).
    - Devuelve una lista con tuplas que contienen la cantidad y el porcentaje por estado.
    Entradas:
    - lista (list): Lista de objetos `Animal`, de los cuales se extrae la información con el método `getDatos()`.
    Salidas:
    - list: Lista de 5 tuplas, cada una representando un estado del 1 al 5 en el formato `(cantidad, porcentaje)`.
    """
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
    """
    Funcionamiento:
    - Permite avanzar de pestaña dentro del inventario.
    Entradas:
    - vtn: Es la ventana del inventario.
    - lista(list): Es la lista con los objetos.
    Salidas:
    - Modifica el índice y muestra 4 animales distintos.
    """
    global indice
    if indice+4<len(lista2):
        indice+=4
        mostrarInventario(vtn,lista2,lista,1,1)

def retroceder(vtn,lista,lista2):
    """
    Funcionamiento:
    - Permite retroceder de pestaña dentro del inventario.
    Entradas:
    - vtn: Es la ventana del inventario.
    - lista(list): Es la lista con los objetos.
    Salidas:
    - Modifica el índice y muestra 4 animales distintos.
    """
    global indice
    if indice>=4:
        indice-=4
        mostrarInventario(vtn,lista2,lista,1,1)

def calificar(estrellas,cali,indice,ini,lista):
    """
    Funcionamiento:
    - Permite calificar a cada animal dependiendo de su estado.
    Entradas:
    - estrellas(list): Es una matriz con los botones.
    - cali(int): La calificación que se le va a asignar al animal.
    - indice(int): Es el índice del animal en su grupo de 4.
    - ini(int): Es el punto donde se inicia a contar según la pestaña.
    - lista(list): Es la lista con los objetos.
    Salidas:
    - Cambia los botones y modifica las calificaciones de los animales, guarda la lista de objetos modificada.
    """
    e,c,o,p=lista[ini+indice].getInformacion()
    if c==cali:     #Si se selecciona el que ya está marcado, la calificación vuelve a 1.
        lista[ini+indice].setInformacion(e,1,o,p)
        estrellas[indice][cali-2].config(bg="#6d4224")
    else:
        for i in estrellas[indice]:
            if i!=estrellas[indice][cali-2]:
                i.config(bg="#6d4224")   #Los que no fueron seleccionados se resetean.
        lista[ini+indice].setInformacion(e,cali,o,p)
        estrellas[indice][cali-2].config(bg="#442a14")
    grabar(lista,"laLista")

def cargarImagenes(vtn,lista,lista2):
    """
    Funcionamiento:
    - Carga las imágenes de los animales en el formato correcto para crear los labels y dependiendo del estado puede mostrar una ambulancia, una calavera o un museo.
    Entradas:
    - vtn: Es la ventana del inventario.
    - lista(list): Es la lista con los objetos.
    Salidas:
    - Carga las imágenes de los animales en el formato adecuado y guarda las referencias.
    """
    global imagenes
    imagenes=[]
    imagen=requests.get("https://media.istockphoto.com/id/928418862/es/vector/icono-de-calavera-y-huesos.jpg?s=612x612&w=0&k=20&c=4BTcXgsw_zTLkrf18ZVwol06fZviCwu1T2oDu4-wIaI=")
    imagenPil=Image.open(BytesIO(imagen.content))
    imagenPil=imagenPil.resize((275,210))
    imagenCala=ImageTk.PhotoImage(imagenPil)    #Se carga la imagen de la calavera.
    imagen=requests.get("https://static.vecteezy.com/system/resources/previews/029/338/731/non_2x/ambulance-car-illustration-emergency-medical-service-vehicle-isolated-on-white-background-vector.jpg")
    imagenPil=Image.open(BytesIO(imagen.content))
    imagenPil=imagenPil.resize((275,210))
    imagenAmbu=ImageTk.PhotoImage(imagenPil)    #Se carga la imagen de la ambulancia.
    imagen=requests.get("https://static.vecteezy.com/system/resources/previews/026/633/423/non_2x/museum-icon-symbol-design-illustration-vector.jpg")
    imagenPil=Image.open(BytesIO(imagen.content))
    imagenPil=imagenPil.resize((275,210))
    imagenMus=ImageTk.PhotoImage(imagenPil)   #Se carga el símbolo del museo.
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
            imagenPil=imagenPil.resize((275,210))
            imagenTK=ImageTk.PhotoImage(imagenPil)     #Se guarda la imagen cargada en el formato corecto.
            imagenes.append(imagenTK)
    vtn.imagenes=imagenes

def mostrarInventario(vtn,lista,lista2,cont,ind):
    """Funcionamiento:
    - Muestra de 4 en cuatro las imágenes de los animales, y permite calificarlos mediante los botones.
    Entradas:
    - vtn: Es la ventana del inventario.
    - lista(list): Es la lista con los objetos.
    - cont(int): Es el contador para verificar si las imágenes ya fueron cargadas.
    - ind(int): Es un entero que resetea el índice a 0 si así se necesita.
    Salidas:
    - Muestra las imágenes de los animales en grupos de 4."""
    global indice
    conta=0
    imaBotones=["imagenes/btnEncanta.png","imagenes/btnFavorito.png","imagenes/btnTriste.png","imagenes/btnEnojado.png"]
    if cont==0:
        indice=0
        cargarImagenes(vtn,lista2,lista)
    if ind==0:
        indice=0
    btnsEstrellas=[]
    ini=indice
    fin=ini+4
    px=171
    py=73

    ava=Button(vtn,text="-->",command=lambda: avanzar(vtn,lista2,lista))
    ava.place(x=1005,y=454)

    retro=Button(vtn,text="<--",command=lambda: retroceder(vtn,lista2,lista))
    retro.place(x=70,y=454)

    for m,i in enumerate(lista[ini:fin]):
        estrellas=[]
        mstImg=Label(vtn,image=imagenes[ini+m])
        mstImg.place(x=px,y=py)
        nombreN,nombreC=lista2[ini+m].getNombres()
        frame=Frame(vtn,width=380,height=30,bg="#eeb98f")   #Se crea un marco para poner los nombres.
        frame.place(x=px-50,y=py+245)
        nombres=Label(frame,text=f"{nombreN}, {nombreC}",anchor="center",bg="#eeb98f",font=("Fixedsys"))
        nombres.place(relx=0.5, rely=0.5, anchor="center") 
        for j in range(2,6):
            imgBtnOrden=PhotoImage(file=imaBotones[conta])
            if conta==3:
                conta=0
            else:
                conta+=1
            e,c,o,p=lista2[ini+m].getInformacion()
            if (j in (2,3)) or (j==4 and e in (2,5)) or (j==5 and e==3):
                if j==c:   #Si el animal ya fue calificado el botón se muestra seleccionado.
                    boton=Button(vtn,image=imgBtnOrden,command=lambda cali=j,indice=m: calificar(btnsEstrellas,cali,indice,ini,lista2),bg="#442a14",borderwidth=0, highlightthickness=0)
                    imgBtnOrden.image=imgBtnOrden
                else:
                    boton=Button(vtn,image=imgBtnOrden,command=lambda cali=j,indice=m: calificar(btnsEstrellas,cali,indice,ini,lista2),bg="#6d4224",borderwidth=0,highlightthickness=0)
                    imgBtnOrden.image=imgBtnOrden
            else:
                boton=Button(vtn,image=imgBtnOrden,bg="#6d4224",state=DISABLED,borderwidth=0, highlightthickness=0,)    #Si el animal no puede recibir la calificación, el botón no hace nada.
                imgBtnOrden.image=imgBtnOrden
            if conta==0 or conta==3:
                boton.place(x=px+-38+97*(j-2),y=py+308)
            else:
                boton.place(x=px+-38+97*(j-2),y=py+313)
            estrellas.append(boton)
        btnsEstrellas.append(estrellas)   #Guarda el botón en la matriz de botones.
        px+=470
        if px>800:   #Se modifica la posición para la siguiente imagen.
            px=171
            py+=453