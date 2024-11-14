
# transferencia_producto.py

from almacen import almacen  # Importamos la estructura del almacén

def transferir_producto():
    print("Transferencia de Productos entre Estanterías")
    
    # Solicitar detalles de la transferencia al usuario
    nombre = input("Ingrese el nombre del producto a transferir: ")
    cantidad = int(input("Ingrese la cantidad a transferir: "))
    estanteria_origen = input("Ingrese la estantería de origen (e.g., Estantería A): ")
    estanteria_destino = input("Ingrese la estantería de destino (e.g., Estantería B): ")
    
    # Verificar que ambas estanterías existen
    if estanteria_origen not in almacen:
        print(f"Error: La estantería de origen '{estanteria_origen}' no existe.")
        return
    if estanteria_destino not in almacen:
        print(f"Error: La estantería de destino '{estanteria_destino}' no existe.")
        return

    # Buscar el producto en la estantería de origen
    producto_origen = None
    for producto in almacen[estanteria_origen]:
        if producto['nombre'] == nombre:
            producto_origen = producto
            break

    # Verificar que el producto existe y tiene suficiente cantidad en la estantería de origen
    if producto_origen is None:
        print(f"Error: El producto '{nombre}' no se encuentra en la estantería de origen '{estanteria_origen}'.")
        return
    elif producto_origen['cantidad'] < cantidad:
        print(f"Error: No hay suficiente cantidad de '{nombre}' en '{estanteria_origen}'. Cantidad disponible: {producto_origen['cantidad']}.")
        return

    # Realizar la transferencia
    producto_origen['cantidad'] -= cantidad  # Reducir la cantidad en la estantería de origen

    # Buscar el producto en la estantería de destino
    producto_destino = None
    for producto in almacen[estanteria_destino]:
        if producto['nombre'] == nombre:
            producto_destino = producto
            break

    # Si el producto ya existe en la estantería de destino, aumentar la cantidad
    if producto_destino:
        producto_destino['cantidad'] += cantidad
    else:
        # Si el producto no existe, agregarlo como un nuevo producto
        nuevo_producto = {"nombre": nombre, "cantidad": cantidad, "precio": producto_origen['precio']}
        almacen[estanteria_destino].append(nuevo_producto)

    # Mensaje de éxito
    print(f"Transferencia exitosa: {cantidad} unidades de '{nombre}' transferidas de '{estanteria_origen}' a '{estanteria_destino}'.")

# Llamada a la función principal si ejecutamos este archivo directamente
if __name__ == "__main__":
    transferir_producto()
