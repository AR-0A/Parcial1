
# verificar_estado_almacen.py

from almacen import almacen  # Importamos la estructura del almacén

def verificar_estado_almacen():
    print("Estado del Almacén\n")

    valor_total = 0  # Variable para almacenar el valor total de todos los productos en el almacén

    # Recorrer cada estantería en el almacén
    for estanteria, productos in almacen.items():
        print(f"Estantería: {estanteria}")
        valor_estanteria = 0  # Valor acumulado en la estantería

        # Recorrer cada producto en la estantería
        for producto in productos:
            nombre = producto['nombre']
            cantidad = producto['cantidad']
            precio = producto['precio']
            
            # Calcular el valor total para cada producto y añadirlo al valor de la estantería
            valor_producto = cantidad * precio
            valor_estanteria += valor_producto

            # Mostrar el nombre y cantidad de cada producto
            print(f"  {nombre}: {cantidad} unidades")

        # Mostrar el valor total de la estantería
        print(f"  Valor total de {estanteria}: {valor_estanteria:.2f} €\n")

        # Sumar el valor de la estantería al valor total del almacén
        valor_total += valor_estanteria

    # Mostrar el valor total del almacén al final
    print(f"Valor total del almacén: {valor_total:.2f} €")

# Llamada a la función principal si ejecutamos este archivo directamente
if __name__ == "__main__":
    verificar_estado_almacen()

