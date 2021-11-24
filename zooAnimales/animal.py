class Animal:
    
    _totalAnimales = 0
    
    def __init__(self, nombre, edad, habitat, genero, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona

    def toString(self):
        if (self._zona == None):
            return "Mi nombre es {}, tengo una edad de {}, habito en {} y mi genero es {}".format(self._nombre, self._edad, self._habitat, self._genero)


    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getNombre(self):
        return self._nombre
    
    def setEdad(self, edad):
        self._edad = edad
        
    def getEdad(self):
        return self._edad
    
    def setHabitat(self, habitat):
        self._habitat = habitat
        
    def getHabitat(self):
        return self._habitat
    
    def setGenero(self, genero):
        self._genero = genero
        
    def getGenero(self):
        return self._genero
    
    def setZona(self, zona):
        self._zona = zona
        
    def getZona(self):
        return self._zona

    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls._totalAnimales = totalAnimales
    
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
