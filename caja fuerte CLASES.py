class ClaveIncorrecta(Exception):
    pass

class ClaveNoValida(Exception):
    pass

class Caja(Exception):
    def __init__(self, abierta = False, clave = 0000000000 ):
        self.__abierta = abierta
        self.__clave = clave

    def estaAbierta(self):
        return self.__abierta
        
    def abrir(self, clave):
        if self.__clave == clave:
            self.__abierta = True
            print(f"Acabas de abrir la caja. Estado actual: Abierta = {self.__abierta}\n")
        else:
            raise ClaveIncorrecta()

    def cerrar(self):
        self.__abierta = False
        print(f"Acabas de cerrar la caja. Estado actual de la caja: Cerrada = {self.__abierta}\n") 
        pass
    
    def cambiarClave(self, clave_vieja, clave_nueva):
        if self.__clave != clave_vieja:
            raise ClaveIncorrecta()
        elif len(str(clave_nueva)) != 10:
            raise ClaveNoValida()
        else:
            self.__clave = clave_nueva
            print("\nContraseña correctamente cambiada \n")
            print(f'Estado de la caja: {self.__abierta} \t Contraseña nueva: {self.__clave}')
   
def main():

    try:
####se inicia y muestra el objeto con los atributos predeterminados
        caja = Caja()
        print(f'Estado inicial de la caja de seguridad: Cerrada = {caja.estaAbierta()} \n')
####pido una clave y si esta es coincide cambia el atributo de "abierta" a False, si no lanza una excepcion personalziada.       
        clave = int(input("Introduzca la contraseña: "))
        caja.abrir(clave)
####cierro la caja        
        caja.cerrar()
####pido contra nueva y vieja y si son validas se actualiza.
        clave_vieja = int(input("Introduzca la contraseña antigua: "))
        clave_nueva = int(input("Introduzca la contraseña nueva: "))
        caja.cambiarClave(clave_vieja, clave_nueva)
        
    except ClaveNoValida:
        print("Clave no valida")

    except ClaveIncorrecta:
        print("La Clave actual no es correcta")
   
main()
    
    
