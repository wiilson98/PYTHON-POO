from math import sqrt
import math
class Taxi:
    def __init__(self, matricula:str, conductor:str, posX:float, posY:float):
        self.matricula = matricula
        self.conductor = conductor
        self.posX = posX
        self.posY = posY

    def __str__(self):
        return f"Matricula: {self.matricula} Conductor: {self.conductor} posX: {self.posX} posY: {self.posY}"
    
class TaxiFurgon(Taxi):
    def __init__(self, matricula:str, conductor:str, posX:float, posY:float, npasajeros:int, carga:int):
        Taxi.__init__(self, matricula, conductor, posX, posY)
        self.npasajeros = npasajeros
        self.carga = carga

    def __str__(self):
        return f"{Taxi.__str__(self)} Npasajeros: {self.npasajeros} CargaMáx: {self.carga}"

class Gestion:
    def __init__(self):
       self.__lista = [Taxi("480", "wil", 200.0, 150.0), Taxi("613", "son", 3.0, 4.0), TaxiFurgon( "7683", "juan", 5.0, 6.0, 7, 200), TaxiFurgon("8F", "benito", 5.0, 6.0, 8, 300)]

        
    def refrescarPosicion(self, matricula:str, nueva_pos_X:float, nueva_pos_Y:float)->None:
        for taxi in self.__lista:
            if taxi.matricula == matricula:
                taxi.posX = nueva_pos_X
                taxi.posY = nueva_pos_Y
            else:
                print("Matricula no existente")

    def obtener(self, matricula:str):
        for taxi in self.__lista:
            if taxi.matricula == matricula:
                return taxi
            else:
                return None

    def distancia(self, posX_A:float, posY_A:float, posX_B:float, posY_B:float)->float:

        return math.sqrt(math.pow(posX_A-posX_B,2) + math.pow(posY_A-posY_B,2))
        
    def buscar(self, pos_X:float, pos_Y:float, distancia):

         return tuple(filter(lambda taxi: self.distancia(pos_X, pos_Y, taxi.posX, taxi.posY) <= distancia , self.__lista))
        
        
    def buscar_carga(self, pos_X, pos_Y, distancia, carga, personas):

        lista_furgones = tuple(filter(lambda taxi: isinstance(taxi, TaxiFurgon), self.__lista))

        return tuple(filter(lambda taxi: self.distancia(pos_X, pos_Y, taxi.posX, taxi.posY) <= distancia and taxi.carga >= carga and taxi.npasajeros >= personas, lista_furgones))
                

def menu():
    while True:
        print("OPCIONES")
        print("1.- Refrescar Posición")
        print("2.- Obtener datos Taxi")
        print("3.- Buscar Taxi")
        print("4.- Buscar Taxi Furgón")
        print("0.- Salir")
        try:
            opcion = int(input("Indica una opcion: "))
            if 0 <= opcion <= 4:                                       
                return opcion
            else:
                print("Opcion incorrecta.")
        except ValueError:
            print("Valor no valido.")


def main():

    gestor = Gestion()
    while True:
        opcion = menu()
        
        if opcion == 1:
            print("REFRESACR POSICIÓN\n")
            matricula = input("Introduzca la matricula: ")
            nueva_pos_X = float(input("Introduzca la nueva posicion X: "))
            nueva_pos_Y = float(input("Introduzca la nueva posicion Y: "))
            gestor.refrescarPosicion(matricula, nueva_pos_X, nueva_pos_Y)

        if opcion == 2:
            print("OBTENER DATOS TAXI\n")
            matricula = input("Introduzca la matricula: ")
            print(gestor.obtener(matricula))

        if opcion == 3:
            print("BUSCAR TAXI\n")
            pos_X = float(input("Introduzca la posicion X: "))
            pos_Y = float(input("Introduzca la posicion Y: "))
            pregunta = input("La distancia sera de 5 unidades. Desea cambiarla(s/n): ").lower()
            if pregunta == "s":
                distancia = int(input("Introduzca la nueva distancia: "))
                taxis = gestor.buscar(pos_X, pos_Y, distancia)
                print(f"Los taxis con la distancia menor o igual a {distancia} son:\n")
                for taxi in taxis:
                    print(taxi)
            else:
                distancia = 5
                taxis = gestor.buscar(pos_X, pos_Y, distancia)
                print(f"Los taxis con la distancia menor o igual a {distancia} son:\n")
                for taxi in taxis:
                    print(taxi)

        if opcion == 4:
            print("BUSCAR TAXI FURGÓN\n")
            pos_X = float(input("Introduzca la posicion X: "))
            pos_Y = float(input("Introduzca la posicion Y: "))
            pregunta = input("La distancia sera de 5 unidades.La carga 0 y el numero de personas 0. Desea cambiarla(s/n): ").lower()
            if pregunta == "s":
                distancia = int(input("Introduzca la nueva distancia: "))
                carga = int(input("Introduzca la carga: "))
                n_personas = int(input("INtroduzca el numero de personas: "))
                taxis = gestor.buscar_carga(pos_X, pos_Y, distancia, carga, n_personas)
                print(f"Los taxis con la distancia menor o igual a {distancia}, con una carga igual o superior a {carga} y con el numero de pasajeros mayor o igual a {n_personas}, son:\n")
                for taxi in taxis:
                    print(taxi)
            else:
                distancia = 5
                carga = 0
                n_personas = 0
                taxis = gestor.buscar_carga(pos_X, pos_Y, distancia, carga, n_personas)
                print(f"Los taxis con la distancia menor o igual a {distancia}, con una carga igual o superior a {carga} y con el numero de pasajeros mayor o igual a {n_personas}, son:\n")
                for taxi in taxis:
                    print(taxi)
            
main()    

