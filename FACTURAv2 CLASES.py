from datetime import datetime
class Articulo:
    def __init__(self, producto, precio, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio

    def calcularImporte(self):
        return self.cantidad * self.precio

    def __str__(self):
        return (f"{self.producto}\t\t{self.cantidad} Uds.\t{self.precio}Eu/U\t = {self.calcularImporte()} Eur.")

class Venta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.fecha = datetime.now()
        self.articulos = list()

    def comprar(self, articulo:Articulo):
        self.articulos.append(articulo)

    
    def calcular_importe_total(self):
        return sum(map(lambda x: x.precio*x.cantidad, self.articulos))
        

def main():
    
    continuar = True
    nombre = str(input("Introduzca el nombre del vendedor: "))
    venta = Venta(nombre)

    while continuar:
        producto = str(input("Indica el nombre del producto: "))
        precio = int(input("Indica el precio unitario del producto: "))
        unidades = int(input("Indica las unidades vendidas: "))
        
        venta.comprar(Articulo(producto,precio,unidades))
        continuar = input("Quieres vender otro artículo?(si/no): ").lower() == 'si'

    print(f"VENDEDOR: {venta.nombre}")
    print(f"Fecha: {venta.fecha.strftime('%c')}\n")
    
    for articulo in venta.articulos:
        print(articulo)

    
    print(f"El importe total es:{venta.calcular_importe_total()} Euros.")

main()


