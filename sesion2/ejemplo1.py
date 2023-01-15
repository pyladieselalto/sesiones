from abc import  ABC, abstractmethod

class Poligono(ABC):
    @abstractmethod
    def area(self):
        pass

#Otro Objeto
#Con los mismo metodos

class Cuadrado(Poligono):
    def area(self):
        print("El area es 8")

# Erroneo
"""
class Cuadrado(Poligono):
    def area(self,lo):
        print(lo)
"""

C = Cuadrado()
C.area()