from math import sqrt
import functools

class Punto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
       
                       
    def cuadrante(self):
        if self.x >=0 and self.y >=0:
            cuadrante = 1
        elif self.x<=0 and self.y>=0:
            cuadrante = 2
        elif self.x<=0 and self.y<=0:
            cuadrante = 3
        elif self.x>=0 and self.y<=0:
            cuadrante = 4
        return cuadrante
    
    def __str__(self):
        
        return (f"x = {self.x} y = {self.y}")

        
class Vector:
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        

    def distancia(self):
        return sqrt((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)

    
def main():
    
####Obtener y mostrar los 4 puntos en la cuadrante
    p1 = Punto(2, 4)
    c1 = p1.cuadrante()
    print(f"A: {p1}  Cuadrante = {c1}")
    p2 = Punto(5, -3)
    c2 = p2.cuadrante()
    print(f"B: {p2}  Cuadrante = {c2}")
    p3 = Punto(3, -5)
    c3 = p3.cuadrante()
    print(f"C: {p3}  Cuadrante = {c3}")
    p4 = Punto(-5, -3)
    c4 = p4.cuadrante()
    print(f"D: {p4}  Cuadrante = {c4}")

####Obtener y mostrar la distancia entre los dos vectores   
    v1 = Vector(p1, p2)
    print(f"La distancia de v1 es: {v1.distancia()}")
    v2 = Vector(p3, p4)
    print(f"La distancia de v2 es: {v2.distancia()}")
    
####agregar los 4 puntos a la lista y mostrar las cordenadas
    
    plano = [p1, p2, p3, p4]
    print(f"Lista de los 4 puntos {' / '.join(map(str,plano))}")
##    plano.extend([(p1.x, p1.y),(p2.x, p2.y),(p3.x, p3.y),(p4.x, p4.y)])
##    print(f"Lista de los 4 puntos {plano}")
    
####Calcular y mostrar el punto más lejano desde el punto(0,0)
    p_zero = Punto(0,0)
##    
##    punto_lejano1 = Vector(p1, p_zero)
##    d1 = punto_lejano1.distancia()
##    
##    punto_lejano2 = Vector(p2, p_zero)
##    d2 = punto_lejano2.distancia()
##
##    punto_lejano3 = Vector(p3, p_zero)
##    d3 = punto_lejano3.distancia()
##
##    punto_lejano4 = Vector(p4, p_zero)
##    d4 = punto_lejano4.distancia()

####TAMBIEN ASI con LAMBDA:

    p_lejano = max(plano, key = lambda p: Vector(p_zero, p).distancia())
    p_cercano = min(plano, key = lambda p: Vector(p_zero, p).distancia())

    print(f"El punto más lejano a 0,0 es: {p_lejano}")
    print(f"EL punto más cercano a 0,0 es: {p_cercano}")

    
            

if __name__ == "__main__":
    main()
    

                    
