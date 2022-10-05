
class Motor:
    def __init__(self, caballos):
        self.caballos = caballos

    def __str__(self):
        return f"Caballos: {self.caballos}"

class Motor_Explosion(Motor):
    def __init__(self, caballos, cilindros):
        Motor.__init__(self, caballos)
        self.cilindros = cilindros

    def __str__(self):
        return f"Caballos: {self.caballos } Cilindros: {cilindros}"

class Motor_Electrico(Motor):
    def __init__(self, caballos, consumo):
        Motor.__init__(self, caballos)
        self.consumo = consumo
    def __str__(self):
        return f"MOTOR ELECTRICO --> Caballos: {self.caballos} Consumo: {self.consumo}"

class Motor_Gasolina(Motor_Explosion):
    def __init__(self, caballos, cilindros, bujia, carburador):
        Motor_Explosion.__init__(self, caballos, cilindros)
        self.bujia = bujia
        self.carburador = carburador

    def __str__(self):
        return f"MOTOR GASOLINA --> Caballos: {self.caballos} Cilindros: {self.cilindros} Bujia: {self.bujia} \nCarburante: {self.carburador}"

class Motor_Diesel(Motor_Explosion):
    def __init__(self, caballos, cilindros, bares):
        Motor_Explosion.__init__(self,caballos, cilindros)
        self.bares = bares

    def __str__(self):
        return f"MOTOR DIESEL --> Caballos: {self.caballos} Cilindros: {self.cilindros} Bares: {self.bares}"
        
def listado(motores:list)->None:

    for i in range (len(motores)):
        print(f"\n{motores[i]}")

def filtrar(motores:list, potencia:int)->None:
        mayores = list(filter(lambda m: m.caballos > potencia, motores))
        for mayor in mayores:
            print(f"\n {mayor}")
   
def main():

#### creacion de objetos.
    electrico = Motor_Electrico(120, "75kW")
    electrico2 = Motor_Electrico(125, "85kw")
    gasolina = Motor_Gasolina(115, 2.0, "cadena", "gasolina")
    diesel = Motor_Diesel(125, 2.0, 5)
    diesel2 = Motor_Diesel(130, 2.1, 6)
####lista con los objetos.   
    motores = [electrico, electrico2, gasolina, diesel, diesel2]
####Llamada a la funcion "listado(motores)" para mostrar los motores mediante el __Str__.
    listado(motores)
####Pide potencia y llama a "filtrar(motores, potencia)" para mostrar los motores mayores a la potencia indicada.
    potencia = int(input("\nIntroduzca una potencia: "))
    filtrar(motores, potencia)

    
if __name__ == "__main__":
    main()
