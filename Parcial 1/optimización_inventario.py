
# optimización_inventario.py

from almacen import almacen  # Importamos la estructura del almacén

def optimizar_inventario():
    print("Optimización del Inventario\n")
    
    estanteria_mayor_valor = None
    estanteria_menor_cantidad = None
    mayor_valor = 0
    menor_cantidad = float('inf')
    valor_estanteria_menor_cantidad = 0  # Almacena el valor de la estantería con menos productos
    unidades_estanteria_mayor_valor = 0  # Almacena la cantidad de unidades en la estantería con mayor valor

    # Recorrer cada estantería en el almacén
    for estanteria, productos in almacen.items():
        valor_estanteria = 0  # Valor acumulado de la estantería
        cantidad_total_estanteria = 0  # Cantidad total de productos en la estantería

        # Calcular el valor total y la cantidad total en la estantería actual
        for producto in productos:
            cantidad = producto['cantidad']
            precio = producto['precio']
            
            valor_estanteria += cantidad * precio  # Sumar el valor de cada producto
            cantidad_total_estanteria += cantidad  # Sumar la cantidad de cada producto

        # Determinar si esta es la estantería con el mayor valor acumulado
        if valor_estanteria > mayor_valor:
            mayor_valor = valor_estanteria
            estanteria_mayor_valor = estanteria
            unidades_estanteria_mayor_valor = cantidad_total_estanteria  # Almacenar la cantidad de productos

        # Determinar si esta es la estantería con la menor cantidad de productos
        if cantidad_total_estanteria < menor_cantidad:
            menor_cantidad = cantidad_total_estanteria
            estanteria_menor_cantidad = estanteria
            valor_estanteria_menor_cantidad = valor_estanteria  # Almacenar el valor de esta estantería

    # Mostrar los resultados
    print(f"Estantería con el mayor valor acumulado: {estanteria_mayor_valor} con un valor de {mayor_valor:.2f} € y {unidades_estanteria_mayor_valor} unidades")
    print(f"Estantería con la menor cantidad de productos: {estanteria_menor_cantidad} con {menor_cantidad} unidades y un valor de {valor_estanteria_menor_cantidad:.2f} €")

# Llamada a la función principal si ejecutamos este archivo directamente
if __name__ == "__main__":
    optimizar_inventario()


