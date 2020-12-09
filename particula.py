from algoritmos import distanciaeuclidiana
class Particula:
    def __init__(self,id=0, origen_x=0, origen_y=0, destino_x=0, destino_y=0, velocidad=0,red=0, green=0,blue=0):
        self.__id = id          
        self.__origen_x =origen_x
        self.__origen_y =origen_y
        self.__destino_x =destino_x
        self.__destino_y =destino_y    
        self.__velocidad =velocidad
        self.__red =red
        self.__green =green
        self.__blue =blue
        self.__distancia= distanciaeuclidiana(origen_x,destino_x,origen_y,destino_y)

    def __str__(self):
        return (
            'id:' + str(self.__id) + '\n' +
            'origen_x:' + str(self.__origen_x) + '\n' +
            'origen_y:' + str(self.__origen_y) + '\n' +
            'destino_x:' + str(self.__destino_x) + '\n' +
            'destino_y:' + str(self.__destino_y) + '\n' +
            'red:' + str(self.__red) + '\n' +
            'green:' + str(self.__green) + '\n' +
            'blue:' + str(self.__blue) + '\n' +
            'velocidad:' + str(self.__velocidad) + '\n' +
            'Distancia = ' + str("{:.2f}".format(self.__distancia))+ '\n'
        )  

    def to_dict(self):
        return{
            "id":  self.__id ,
	        "origen_x": self.__origen_x,
	        "origen_y":  self.__origen_y,
        	"destino_x": self.__destino_x,
        	"destino_y": self.__destino_y,
	        "red": self.__red,
	        "green": self.__green,
	        "blue": self.__blue,
            "velocidad": self.__velocidad
        } 

    
    @property
    def  Id(self):
        return self.__id
    @property
    def  origen_x(self):
        return self.__origen_x
    @property
    def  origen_y(self):
        return self.__origen_y
    @property
    def  destino_x(self):
        return self.__destino_x
    @property
    def  destino_y(self):
        return self.__destino_y
    @property
    def  velocidad(self):
        return self.__velocidad
    @property
    def  rojo(self):
        return self.__red
    @property
    def  verde(self):
        return self.__green
    @property
    def  azul(self):
        return self.__blue
    @property
    def distancia(self):
        return self.__distancia

    def __lt__(self,other):
        return self.Id < other.Id
    
#l01 = Particula("220203","56","102","89","76","100","78","0","98")
#print(l01)
#l02 = Particula("220204","58","105","99","86","105","88","1","100")
#print(l02)
