from datetime import datetime
class Tienda:
    def __init__(self, nombre:str, lista_final:list):
        
        self.nombre = nombre
        self.producto = lista_final

    def calculo_total(self, lista_precio:list, lista_unidades:list)->float:
        total = 0
        for valor_a, valor_b in zip(lista_precio, lista_unidades):
            total += valor_a * valor_b        
        return total
           
def main():
##"CREO 3 LISTAS Y LES AÑADO LOS INPUTS PEDIDOS" 
    lista_precio = []
    lista_unidades = []
    lista_final = []
    otro = "si"
    
    nombre = str(input("Indica el nombre del vendedor: "))
    while otro == "si":
        producto = str(input("Indica el nombre del producto: "))
        precio = float(input("Indica el precio unitario del producto: "))
        unidades= int(input("Indica las unidades vendidas: "))
        lista_final.append([producto, unidades, precio])
        lista_precio.append(precio)
        lista_unidades.append(unidades)
        otro = str(input("Quieres vender otro artículo?(si/no): ")).lower()
        
##"INICIO LA CLASE Y LA RECORRO PARA MOSTRAR POR PANTALLA" 
    ventas = Tienda(nombre, lista_final)
    
    print(f"\nVENDEDOR: {ventas.nombre}\n")
    fecha = datetime.now()
    print(f"FECHA: {fecha.strftime('%c')}\n")
    for i in ventas.producto:
        print(f"{i[0]}\t\t{i[1]} Uds.\t{i[2]}Eu/U\t = {i[1]*i[2]} Eur.")

##"UTILIZO EL METODO 'calculo_total(..)' PARA OBTENER EL IMPORTE TOTAL.
    print(f"El IMPORTE TOTAL ES: {ventas.calculo_total(lista_precio, lista_unidades)} Euros.")
    

if __name__ == "__main__":
    main()
    

    
                   
