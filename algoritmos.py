import math

def distanciaeuclidiana(x_1,y_1,x_2,y_2):
    sq1 = (x_1 - x_2) * (x_1 - x_2)
    sq2 = (y_1 - y_2) * (y_1 - y_2)
    return round(math.sqrt(sq1 + sq2))

