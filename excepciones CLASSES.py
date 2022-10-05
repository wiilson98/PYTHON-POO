class Error(Exception):
    pass


def main():

    try:
        print("Codigo 1:")
        resultado = 20/0

    except ZeroDivisionError:
        print(Error("No es posible divir entre 0."))

    try:

        print("Codigo 2:")
        lista = [ 1,2,3,4 ]
        print(lista[10])

    except IndexError:
        print(Error("Indice fuera de rango"))

    try:
        print("Codigo 3:")
        capitales = {"Francia":"Paris", "Inglaterra":"Londres", "España":"Madrid"}
        print(capitales("Italia"))
        
    except TypeError:
        print(Error("Clave no existente"))

    try:
        print("Codigo 4:")
        suma = "10" + 10

    except TypeError:
        print(Error("No se puede sumar str con enteros"))


if __name__ == "__main__":
    main()





##
##lista = [1, 2, 3, 4, 5]
##numero = 5
##
##class Error(Exception):
##    pass
##
##def agregarUnico(lista:list, valor:int):
##
##    if numero not in lista:
##        lista.append(numero)
##        print(lista)
##    else:
##        raise ValueError
##
##
##def main():
##    try:
##        agregarUnico(lista, numero)
##
##    except ValueError:
##
##        print(Error(f"El número {numero} ya está en la lista."))
##
##main()
##        
##
                        
