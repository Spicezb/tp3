class Animal:
    # Definición de atributos
    id = ""
    nombres = ()
    url = ""
    informacion = []
    
    # Definición de los métodos
    def __init__(self):
        self.id = ""
        self.nombres = ()
        self.url = ""
        self.informacion = []
    
    def setId(self,idN):
        self.id = idN
    
    def setNombres(self,nombres):
        self.nombres = (nombres)
    
    def setURL(self,urlN):
        self.url = urlN
    
    def setInformacion(self,estado,calificacion,orden,peso):
        self.informacion = [estado,calificacion,orden,peso]
    
    def getId(self):
        return self.id
    
    def getNombres(self):
        return self.nombres
    
    def getURL(self):
        return self.url
    
    def getInformacion(self):
        return self.informacion
    
    def getDatos(self):
        return (self.id,self.nombres,self.url,self.informacion)
    





html+=f"""
                <tr>
                <td>{x[3][3]}</td>
                <td>{x[1][0]}</td>
                </tr>"""