class Livro:
    #construtor
    def __init__(self, titulo, autor, genero, situacao):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__situacao= situacao
    # ----------------------------------------------------------------------
# Metódos GETS and SETs 
#GETs

def getTitulo(self):
    return self.__titulo

def getAutor(self):
    return self.__autor

def getGenero(self):
    return self.__genero

def getSituacao(self):
    return self.__situacao

#SETs 
def setTitulo(self,titulo):
    self.__titulo = titulo
    return self.__titulo

def setAutor(self,autor):
    self.__autor = autor
    return self.__autor

def setGenero(self,genero):
    self.__genero = genero
    return self.__genero

def setSituacao(self,situacao):
    self.__situacao = situacao
    return self.__situacao

