##class Cuenta:
##    def __init__(self, ncuenta, titular, saldo = 0, interes = 0, edad = 0):
##        self.ncuenta = ncuenta
##        self.titular = titular
##        self.saldo = saldo
##        self.interes = interes
##        self.edad = edad
##
##    def ingreso(self, cantidad):
##        self.saldo = self.saldo + cantidad
##
##    def reintegro(self,cantidad):
##        self.saldo = self.saldo - cantidad
##
##    def getBeneficio(self):
##        return self.saldo * (self.interes/100)
##
##        
##
##def main():
##
##    objCuenta = Cuenta(10234, "Wilson", 1200, 0.4, 20)
##
##    
##    print("El titular es: " + objCuenta.titular)
##    print("El saldo es: " + str(objCuenta.saldo))
##    print("EL interes es: " + str(objCuenta.interes))
##    print("----------------------------------")
##
##    objCuenta.titular = "pacheko"
##    objCuenta.ingreso(500)
##    objCuenta.reintegro(200)
##    objCuenta.interes = 0.5
##
##    def cumpleaños(Cuenta):
##        Cuenta.edad = Cuenta.edad + 1
##    cumpleaños(objCuenta)
##    
##
##    print("El juevo titular es: " + objCuenta.titular)
##    print("EL nuevo saldo es: " + str(objCuenta.saldo))
##    print("EL nuevo interes es: " + str(objCuenta.interes))
##    print("La edad sumada con la funcion es: " + str(objCuenta.edad))
##


##main()
##    
##class Persona :
##    
##    def __init__(self, nombre, edad, altura):
##        
##        self.__nombre = nombre
##        self.__edad = edad
##        self.__altura = altura
##        
##    @property
##    def get_nombre(self):
##        return self.__nombre
##    @property
##    def get_edad(self):
##        return self.__edad
##    @property
##    def get_altura(self):
##        return self.__altura
##    @edad.setter    
##    def set_edad(self):
##        if edad > 0:
##            self.__edad = edad
##    @altura.setter  
##    def set_altura(self):
##        if altura > 0:
##            self.__altura = altura
##
##           
##
##def main():
##
##
##    obj = Persona( "WILSON", 23, 1.65)
##    
##    print(f"{obj.get_nombre()}, tiene {obj.get_edad()} años y mide {obj.get_altura()} cm")
##
##    
##main()



##class Cliente:
##    def __init__ (self, nombre, direccion, telefono, email):
##        self.nombre = nombre
##        self.direccion = direccion
##        self.telefono = telefono
##        self.email = email
##
##class Cuenta:
##
##    def __init__ (self, ncuenta, titular, saldo=0, interes=0):
##        self.ncuenta = ncuenta
##        self.titular = titular
##        self.__saldo = saldo
##        self.__interes = interes
##    @property
##    def saldo(self):
##        return self.__saldo
##    @property
##    def interes(self):
##        return self.__interes
##    def ingresar (self, cantidad):
##        self.__saldo += cantidad
##    def retirar (self, cantidad):
##        self.__saldo -= cantidad
##    def obtener_beneficio(self):
##        return self.__saldo * self.__interes
##class CuentaBonificada(Cuenta):
##    def __init__(self, ncuenta, titular, saldo=0, interes=0, bonificacion=0):
##        super().__init__(ncuenta, titular, saldo, interes)
##        self.__bonificacion = bonificacion
##    @property
##    def bonificacion(self):
##        return self.__bonificacion
##    def obtener_beneficio(self):
##        return super().obtener_beneficio() + self.__bonificacion
##                    
##def main():
##    # Creacion del objeto cliente
##    obj_cliente = Cliente("Roger Petrovich", "C/Ulianov, 25", "555-493021", "none@none.ru")
##    # Creacion del objeto cuenta
##    obj_cuenta = Cuenta("123-456", obj_cliente, 1250.50, 0.7 )
##    print("Beneficios {0:.2f}".format(obj_cuenta.obtener_beneficio()))
##    # Creacion del objeto cuentaBonificada
##    obj_cuenta_bonificada = CuentaBonificada("123-456-B", obj_cliente, 1250.50, 0.7, 100 )
##    print("Beneficios {0:.2f}".format((obj_cuenta_bonificada.obtener_beneficio())))
##    
##if __name__ == "__main__":
##    main()
##
##
##
##
##class Cuadrado:
##    def __init__(self, alto, ancho):
##        self.__alto = alto
##        self.__ancho = ancho
##    def mostrar(self):
##        return "Alto: {}. Ancho {}.".format(self.__alto, self.__ancho)
##class FiguraMapa:
##    def __init__(self, x, y):
##        self.__x = x
##        self.__y = y
##    def mostrar(self):
##        return "X: {}. Y: {}".format(self.__x, self.__y)
##class CuadradoMapa(Cuadrado, FiguraMapa):
##    def __init__(self, alto, ancho, x, y, identificacion):
##        Cuadrado.__init__(self, alto, ancho)
##        FiguraMapa.__init__(self, x, y)
##        self.__identificacion = identificacion
##    def mostrar(self):
##        return "Cuadrado: {} {} en {}".format(self.__identificacion, Cuadrado.mostrar(self), FiguraMapa.mostrar(self))
##def main():
##    c = CuadradoMapa(100,200,1,2,"Cuadradonumero1")
##    print(c.mostrar())
##    pass
##if __name__ == "__main__":
##    main()

##class Articulo: # INFO PRODUCTO
##    def __init__(self, producto, cantidad, precio):
##        self.producto = producto
##        self.cantidad = cantidad
##        self.precio = precio
##
##    def calcular_importe(self):
##        return self.cantidad * self.precio
##
##
##class Venta: # LO QUE VENDO
##    def __init__(self, nombre, articulos):
##        self.nombre = nombre
##        self.articulos = articulos
##
##    def calcular_importe_total(self):
##        importe = 0
##        for i in self.articulos:
##            importe = importe + i.calcular_importe()
##        return importe
##
##def main():
##
##    objART1 = Articulo("Tornillos", 2, 5)
##    objART2 = Articulo("Tuercas   ", 3, 3)
##    objVENTA = Venta("Manolo", [objART1, objART2])
##
##    print(f"VENDEDOR: {objVENTA.nombre}")
##
##    for objProducto in objVENTA.articulos:
##        print(f"{objProducto.producto}\t{objProducto.cantidad} Uds.\t{objProducto.precio} Eu/U\t= {objProducto.calcular_importe()} Eur.")
##
##    print(f"El importe final: {objVENTA.calcular_importe_total()}")
##    
##
##    
##
##main()
    

cuentas = {}
class Cuenta:
    def __init__(self, ncuenta, titular, saldo = 0, interes = 0):
        self.ncuenta = ncuenta
        self.titular = titular
        self.saldo = saldo
        self.interes = interes

    def ingreso(self, cantidad):
        self.saldo = self.saldo + cantidad

    def reintrego(self, cantidad):
        self.saldo = self.saldo - cantidad

    def get_beneficio(self):
        return self.saldo * (self.interes/100)

def menu():
    print("Opciones:")
    print("1.-ALTA DE CUENTA")
    print("2.-BAJA DE CUENTA")
    print("3.-LISTA DE CUENTAS")
    print("0.-SALIR\n")
    return input("Seleccione una opcion: ")

def alta():
    print("ALTA")
    ncuenta = input("Introduzca el número de cuenta: ")
    if ncuenta not in cuentas:
        titular = input("Indica titular: ")
        saldo = float(input("Indica saldo: "))
        interes = float(input("Indica interes: "))
        objeto = Cuenta(ncuenta, titular, saldo, interes)
        cuentas[ncuenta] = objeto
        print("Cuenta registrada correctamente")
    else:
        print("Cuenta ya existente")

def baja():
    print("BAJA")
    ncuenta = input("Introduzca el numero de cuenta: ")
    if ncuenta in cuentas:
        del(cuentas[ncuenta])
        print("Cuenta eliminada")
    else:
        print("Cuenta no existente\n")

def movimiento():
    
    ncuenta = input("Introduzca el numero de cuenta: ")
    
    if ncuenta not in cuentas:
        print("Cuenta inexistente.")
        

    cantidad = int(input("Introduzca una cantidad: "))
    if cantidad < 0:
        print("Cantidad incorrecta. ")
    
    pregunta = input("Ingreso o Reintrego.(I/R): ").lower()
    if pregunta == "r" and if cantidad - objeto.saldo < 0:
        cuentas[ncuenta] = [
    
    
            

def listar():
    if len(cuentas) == 0:
        print("No hay cuentas registradas. ")
    print("LISTA DE CUENTAS\n")
    for ncuenta, cuenta in cuentas.items():
        print(f"Cuenta: {cuenta.ncuenta}")
        print(f"Titular: {cuenta.titular}")
        print(f"Saldo: {cuenta.saldo}")
        print(f"Interes: {cuenta.interes}")

    print("Fin lista")
    
        
    

def main():

    while True:
        opcion = menu()

        if opcion == "1":
            alta()
        elif opcion == "2":
            baja()
        elif opcion == "3":
            listar()
        elif opcion == "4":
            movimiento()
        elif opcion == "0":
            break
    print("Fin del programa")

if __name__ == "__main__":
    main()
    




















