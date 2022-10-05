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
    print("4.-MOVIMIENTO")
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

def movimiento():
    
    print("MOVIMIENTO")
    ncuenta = input("Introduzca el numero de cuenta: ")
    while ncuenta not in cuentas:
        print("Cuenta inexistente.")
        ncuenta = input("Introduzca el numero de cuenta: ")
        
    cantidad = int(input("Introduzca una cantidad: "))
    while cantidad < 0:
            print("Cantidad incorrecta. ")
            cantidad = int(input("Introduzca una cantidad: "))
    
    pregunta = input("Ingreso o Reintrego.(I/R): ").lower()
    if pregunta == "i":
        saldo_sumado = cuentas[ncuenta].saldo + cantidad
        cuentas[ncuenta].saldo =  saldo_sumado
        print("Cantidad ingresada correctamente")

    elif pregunta == "r" and  cuentas[ncuenta].saldo < cantidad:
        print("Saldo insuficiente")
        
    else:
        saldo_restado = cuentas[ncuenta].saldo - cantidad
        cuentas[ncuenta].saldo =  saldo_restado
        print("Cantidad restada correctamente")

    

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
    
