class CuentaDesconocidaError(Exception):
    pass
class ClienteDesconocidoError(Exception):
    pass
class CuentaDuplicadaError(Exception):
    pass
class ClienteDuplicadoError(Exception):
    pass
class saldoError(Exception):
    pass
class interesError(Exception):
    pass
class saldoInsuficienteError(Exception):
    pass
class bonificacionError(Exception):
    pass

class Cliente:
    
    def __init__(self, dni:str, nombre:str, direccion:str, telefono:str,email:str):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion 
        self.telefono = telefono
        self.email = email

class Cuenta:

    def __init__(self, ncuenta:int , cliente:Cliente,  saldo:float, interes:float):
        self.ncuenta = ncuenta
        self.cliente = cliente
        self.saldo =  saldo
        self.interes = interes 


class CuentaBonificada(Cuenta):
    def __init__(self, ncuenta:int , titular:Cliente, saldo:float, interes:float, bonificacion:float):
        Cuenta.__init__(self, ncuenta, titular, saldo, interes)
        self.bonificacion = bonificacion 


class Gestion:
    
    def __init__(self):
        
        self.__clientes = {'480': ('Leo', 'calle', '666', '@'), '613': ('cr7', 'avenida', '900', '@')}
        self.__cuentas = {11: ({'480': ('Leo', 'calle', '666', '@')}, 2600.0, 0.1), 22: ({'480': ('Leo', 'calle', '666', '@')}, 45.0, 0.2), 33: ({'613': ('cr7', 'avenida', '900', '@')}, 1800.0, 0.3), 44: ({'613': ('cr7', 'avenida', '900', '@')}, 90.0, 0.4)}
        
##        self.__clientes = {}
##        self.__cuentas = {}
    def altaCliente(self, cliente)->None:
        
        if cliente.dni not in  self.__clientes:
            self.__clientes[cliente.dni] = cliente.nombre, cliente.direccion, cliente.telefono, cliente.email
        else:
            raise ClienteDuplicadoError()
            
    def bajaCliente(self, dni:str)->None:
        
        if dni in self.__clientes:
            del self.__clientes[dni]
        else:
            raise ClienteDesconocidoError()
        
    def obtenerCliente(self, dni:str)->dict:
        
        dict2 = {}
        if dni in self.__clientes:
            for clave, valor in self.__clientes.items():
                if dni == clave:
                    dict2[clave] = valor
                    return dict2
        else:
            raise ClienteDesconocidoError()


    def listarClientes(self)->tuple:
        
        return tuple(self.__clientes.items())

    def altaCuenta(self, cuenta)->None:
        
        if cuenta.ncuenta not in self.__cuentas:
            
            self.__cuentas[cuenta.ncuenta] = cuenta.cliente, cuenta.saldo, cuenta.interes
        else:
            raise cuentaDuplicadaError()
        
    def altaCuentaBonificada(self, cuenta)->None:
        
        if cuenta.ncuenta not in self.__cuentas:
            
            self.__cuentas[cuenta.ncuenta] = cuenta.cliente, cuenta.saldo, cuenta.interes, cuenta.bonificacion
        else:
            raise cuentaDuplicadaError()
        
    def bajaCuenta(self, ncuenta:int)->None:
        
        if ncuenta in self.__cuentas:
            del self.__cuentas[ncuenta]
        else:
            raise CuentaDesconocidaError()

    def obtenerCuenta(self, ncuenta:int)->dict:
        
        dict3 = {}
        if ncuenta in self.__cuentas:
            for clave, valor in self.__cuentas.items():
                if ncuenta == clave:
                    dict3[clave] = valor
                    return dict3
        else:
            raise CuentaDesconocidaError()

    def listarCuentasCliente(self, dni:str)->tuple:

        dict4 = {} 
        if dni in self.__clientes:
            for clave, valor in self.__cuentas.items():
                cliente, *resto = valor
                for clave2, valor2 in cliente.items():
                    if dni == clave2:
                        dict4[clave] = valor
            return tuple(sorted(dict4.items(), key = lambda i: i[1]))  
        else:
            raise ClienteDesconocidoError()

    def saldoCuentasCliente(self, dni:str, bonificadas:bool)->int:
        dict7 = {}       
        if dni in self.__clientes:
            for clave, valor in self.__cuentas.items():
                cliente, *resto = valor
                for clave2, valor2 in cliente.items():
                    if dni == clave2:
                        dict7[clave] = valor
            suma_saldo = 0
            if bonificadas == True:
                for valor3 in dict7.values():
                    if len(valor3) == 4:
                        cliente, saldo , interes , bonificacion = valor3
                        suma_saldo += saldo
                return suma_saldo
            else:
                total = 0
                suma_saldo2 = 0
                suma_saldo3 = 0
                for valor3 in dict7.values():
                    if len(valor3) == 3:
                        cliente, saldo , interes = valor3
                        suma_saldo2 += saldo
                
                for valor4 in dict7.values():
                    if len(valor4) == 4:
                        cliente, saldo , interes , bonificacion = valor4
                        suma_saldo3 += saldo
                total = suma_saldo2 + suma_saldo3
                return total
        else:
            raise ClienteDesconocidoError()   
        
    def cuentasRiesgo(self)->tuple:

        dict5 = {}
        for clave, valor in self.__cuentas.items():
            cliente, saldo, *resto = valor
            if saldo < 100:
                dict5[clave] = valor
        return tuple(dict5.items())
        
    def clientesPreferentes(self, dni:str)->tuple:

        dict6 = {}
        if dni in self.__clientes:
            for clave, valor in self.__cuentas.items():
                cliente, *resto = valor
                for clave2, valor2 in cliente.items():
                    if dni == clave2:
                        dict6[clave] = valor
            return tuple(sorted(dict6.values()))
                
        else:
            raise ClienteDesconocidoError()


    def ingreso(self, valor:float, ncuenta:int)->None:
        
        if ncuenta in self.__cuentas:
            if valor > 0:
                cliente,saldo,*resto  = self.__cuentas[ncuenta]
                self.__cuentas[ncuenta] = cliente, saldo + valor, *resto
                
            else:
                raise saldoError()
        else:
            raise CuentaDesconocidaError()

    def reintegro(self, valor:float, ncuenta:int)->None:

        if ncuenta in self.__cuentas:
            if valor > 0:
                if self.__cuentas[ncuenta][1] > valor:
                    cliente,saldo,*resto  = self.__cuentas[ncuenta]
                    self.__cuentas[ncuenta] = cliente, saldo - valor, *resto
                else:
                    raise saldoInsuficienteError()
            else:
                raise saldoError()
        else:
            raise CuentaDesconocidaError()

    
    def obtenerRendimiento(self, ncuenta:int)->float:
        
        if ncuenta in self.__cuentas:
            return self.__cuentas[ncuenta][1] * (self.__cuentas[ncuenta][2]/100)
        else:
            raise CuentaDesconocidaError()

    
    def transferenciaCuentas(self, ncuenta1:int, ncuenta2:int, valor:float)->None:
        
        if ncuenta1 and ncuenta2 in self.__cuentas:
            if valor > 0 and valor < self.__cuentas[ncuenta1][1]:
                cliente,saldo,*resto  = self.__cuentas[ncuenta1]
                self.__cuentas[ncuenta1] = cliente, saldo - valor, *resto
                
                cliente2,saldo2,*resto2  = self.__cuentas[ncuenta2]
                self.__cuentas[ncuenta2] = cliente2, saldo2 + valor, *resto2
            else:
                raise saldoError()
        else:
            raise CuentaDesconocidaError()
        



                   
             
def menu():   
    while True:
        print("OPCIONES")
        print("1.- ALTA CLIENTE")
        print("2.- BAJA CLIENTE")
        print("3.- OBTENER CLIENTE")
        print("4.- LISTA DE CLIENTES")
        print("5.- ALTA DE CUENTA")
        print("6.- BAJA DE CUENTA")
        print("7.- OBTENER CUENTA")
        print("8.- LISTA CUENTAS CLIENTES")
        print("9.- SALDO CUENTAS CLIIENTE")
        print("10.- CUNETAS RIESGO")
        print("11.- CLIENTES PREFERENTES")
        print("12.- INGRESO a CUENTA")
        print("13.- REINTEGRO a CUENTA")
        print("14.- OBTENER RENDIMIENTO CUENTA")
        print("15.- TRANSFERENCIA ENTRE CUENTAS")
        print("0.- SALIR")
        try:
            opcion = int(input("Indica una opcion: "))
            if opcion >= 0 and opcion <= 15:
                return opcion
            else:
                print("Opcion incorrecta.")
        except ValueError:
            print("Valor no valido.")

def main():        
    gestor = Gestion()
    while True:
        try:
            opcion = menu()
            
            if opcion == 1:
                print("ALTA DE CLIENTE\n")
                dni = input("Introduzca el dni: ")
                nombre = input("Introduzca el nombre: ")
                direccion = input("Introduzca la direccion : ")
                telefono = input("Introduzca el telefono: ")
                email = input("Introduzca el email: ")
                cliente = Cliente(dni, nombre, direccion, telefono, email)
                gestor.altaCliente(cliente)
                print("Cliente registrado correctamente.\n")                
               
            elif opcion == 2:
                print("BAJA DE CLIENTE\n")
                dni = input("Introduzca el dni: ")
                gestor.bajaCliente(dni)
                print("Cliente dado de baja correctamente.\n")
                
            elif opcion == 3:
                print("OBTENER DATOS DE UN CLIENTE\n")
                dni = input("Introduzca el dni: ")
                print(gestor.obtenerCliente(dni))
                print("Fin datos cliente.\n")
                
            elif opcion == 4:
                print("LISTA DE CLIENTES\n")
                tupla_clientes = gestor.listarClientes()
                print(tupla_clientes)                              
                print("Fin lista clientes.\n")
                
##            "Para las cuentas bonificadas he creado un método más en gestión llamado CuentaBonificada, que introduce la bonificacion al mismo diccionario self.__cuentas"
            
            elif opcion == 5:
                print("ALTA DE CUENTA\n")
                dni = input("Introduzca el dni: ")
                ncuenta = int(input("Introduzca el número de cuenta: "))
                saldo = float(input("Introduzca el saldo: "))
                if saldo < 0:
                    raise saldoError()
                interes = float(input("Introduzca el interés: "))
                if interes < 0.05 or interes > 5.0:
                    raise interesError()
                pregunta = input("Desea que le cuenta sea bonificada?(s/n): ").lower()
                if pregunta == "n":
                    cuenta = Cuenta(ncuenta, gestor.obtenerCliente(dni), saldo, interes)
                    gestor.altaCuenta(cuenta)
                else:
                    bonificacion = float(input("Introduzca la bonifiacion: "))
                    if bonificacion < 10 or bonificacion > 100:
                        raise bonificacionError()
                    cuenta = CuentaBonificada(ncuenta, gestor.obtenerCliente(dni), saldo, interes, bonificacion)
                    gestor.altaCuentaBonificada(cuenta)
                print("Cuenta con cliente regitrada correctamente.\n")

            elif opcion == 6:
                print("BAJA DE CUENTA\n")
                ncuenta = int(input("Introduzca el número de cuenta: "))
                gestor.bajaCuenta(ncuenta)
                print("Cuenta dada de baja correctamente.\n")

            elif opcion == 7:
                print("OBTENER DATOS DE UNA CUENTA")
                ncuenta = int(input("Introduzca el nùmero de cuenta: "))
                print(gestor.obtenerCuenta(ncuenta))
                print("Fin datos cuenta.")

            elif opcion == 8:
                dni = input("Introduzca el dni: ")
                tupla_cliente = gestor.listarCuentasCliente(dni)
                print(tupla_cliente) 
                print("Fin cuentas cliente.")

##            "Si el argumento es 'False' retorna el sumatorio de cuentas normales y bonificadas(del dni indicado). Por el contrario solo retorna el sumatorio de saldos de cuentas bonificadas"
            
            elif opcion == 9:
                print("SUMA SALDOS CLIENTE.")
                dni = input("Introudzca el dni: ")
                bonificadas = False
                suma_saldos=gestor.saldoCuentasCliente(dni, bonificadas)
                print(f"La suma de saldos de las cuentas con el numero de dni {dni} es de: {suma_saldos} $.")
                

            elif opcion == 10:
                print("CUENTAS DE RIESGO.\n")
                saldos = gestor.cuentasRiesgo()
                print(f"La suma de saldos es: {saldos}")
                
            elif opcion == 11:
                print("CLIENTES PREFERENTES.\n")
                dni = input("Introduzca el dni: ")
                preferentes = gestor.clientesPreferentes(dni)
                print(preferentes)
                print("FIN CLIENTES PREFERENTES.")
                
            elif opcion == 12:
                ncuenta = int(input("Introduzca el número cuenta: "))
                valor = float(input("Introduzca la cantidad: "))
                gestor.ingreso(valor, ncuenta)
                print("Ingreso realizado correctamente.\n")

            elif opcion == 13:
                ncuenta = int(input("Introduzca el número cuenta: "))
                valor = float(input("Introduzca la cantidad: "))
                gestor.reintegro(valor, ncuenta)
                print("Reintegro realizado correctamente.\n")

            elif opcion == 14:
                print("OBTENER RENDIMIENTO DE CUENTA")
                ncuenta = int(input("Introduzca el número cuenta: "))
                rendimiento = gestor.obtenerRendimiento(ncuenta)
                print(f"El rendimiento de la cuenta seria de: {rendimiento} $.")
                
##          "Pido dos numeros de cuenta y una cantidad. y en el metodo resto al origen y suma al destino."
                
            elif opcion == 15:
                print("TRANSFERENCIA ENTRE CUENTAS")
                ncuenta1 = int(input("Introduzca el origen de la transferencia: "))
                ncuenta2 = int(input("Introduzca el destino de la transferencia: "))
                valor = float(input("Introduzca el valor de la transferencia: "))
                gestor.transferenciaCuentas(ncuenta1, ncuenta2,valor)
                print("Tranferencia realiazada correctamente.\n")
                
##         " En todos los métodos capturo posibles excepciones con los posibles saldos negativos"            
                                   
            else:
                print("adios")
                break
            
        except CuentaDesconocidaError:
            print("Error. Cuenta no existente.\n")
        except ClienteDesconocidoError:
            print("Error. Cliente no existente.\n")  
        except CuentaDuplicadaError:
            print("Error. Este número de cuenta ya está registrado.\n")
        except ClienteDuplicadoError:
            print("Error. Cliente con DNI ya registrado.\n")
        except saldoError:
            print("Error saldo insuficiente o valor negativo o fuera de rango.\n")
        except interesError:
            print("Error. Ineteres negativo o fuera de rango.\n")
        except saldoInsuficienteError:
            print("Error. Valor superior al saldo de la cuenta.\n")
        except bonificacionError:
            print("Error. Bonificacion negativa o fuera de rango.\n")
            
                              
            
if __name__ == "__main__":
    main()
