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
    
    def setNombres(self,nombreN,nombreC):
        self.nombres = (nombreN,nombreC)
    
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